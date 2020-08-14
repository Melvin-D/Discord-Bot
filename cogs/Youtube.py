import discord
import os
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

class Youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='play')
    async def playFromYT(self, ctx, url):
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
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/song.mp3"))

    @commands.command(name='leave')
    async def leave(self, ctx):
        server = ctx.message.guild.voice_client
        await server.disconnect()
        os.remove("song.mp3")

def setup(bot):
    bot.add_cog(Youtube(bot))