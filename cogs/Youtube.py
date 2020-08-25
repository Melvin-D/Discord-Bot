import discord
import os
import asyncio
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
from time import sleep

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

class Youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play')
    async def playFromYT(self, ctx, url = None):
        
        if url is None:
            await ctx.send(f"{ctx.author.mention} !play [YouTube URL]")
            return

        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return

        options = {
                "postprocessors":[{
                    "key": "FFmpegExtractAudio", # download audio only
                    "preferredcodec": "mp3", # other acceptable types "wav" etc.
                    "preferredquality": "192" # 192kbps audio
                }],
                "format": "bestaudio/best",
                "outtmpl": "song.mp3" # downloaded file name
                }


        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([url])
                
            
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
        video_description = info_dict.get('description', None)
        video_duration = info_dict.get('duration', None)
        video_views = info_dict.get('view_count', None)
            
        channel = ctx.author.voice.channel
        voice = await channel.connect() 
        await ctx.send(embed= discord.Embed(title=f"Now playing: {video_title}", description=f"**Views: {video_views:,d} \n Video length: {video_duration}s** \n \n {video_description}", color=0xFF0000))
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/song.mp3"))

        while voice.is_playing():
            await asyncio.sleep(1)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=video_title))
                
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="server chat"))
        await self.leave(ctx)
            
        

    @commands.command(name='leave')
    async def leave(self, ctx):
        server = ctx.message.guild.voice_client
        await server.disconnect()
        os.remove("song.mp3")

    # @commands.command(name='ytsearch')
    # async def ytsearch(self, ctx, query = None):
    #     options = {
    #             "postprocessors":[{
    #                 "key": "FFmpegExtractAudio", # download audio only
    #                 "preferredcodec": "mp3", # other acceptable types "wav" etc.
    #                 "preferredquality": "192" # 192kbps audio
    #             }],
    #             "format": "bestaudio/best",
    #             "outtmpl": "song.mp3" # downloaded file name
    #         }

    #     with youtube_dl.YoutubeDL(options) as ydl:
    #         video = ydl.extract_info(f"ytsearch:{query}", download = False) ['entries'] [0]
    #         videoUrl = video.get('video_url', None)
    #         await self.playFromYT(ctx, videoUrl)


    # @commands.command(name='pause')
    # async def pause(self,ctx):
    #     await ctx.send("YouTube clip paused")
    #     server = ctx.message.guild.voice_client
    #     server.pause()
        
        
    # @commands.command(name='resume')
    # async def resume(self,ctx):
    #     await ctx.send("Resuming YouTube clip")
    #     server = ctx.message.guild.voice_client
    #     server.resume()

def setup(bot):
    bot.add_cog(Youtube(bot))