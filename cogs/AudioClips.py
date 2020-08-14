import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from time import sleep

class AudioClips(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='SUB', help = "When someone says some dumb ass take")
    async def playTheRockSUB(self, ctx):
        if ctx.author.voice is None:
             await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
             await ctx.send(name)
             return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/SUB.mp3"))
        sleep(1.2)
        server = ctx.message.guild.voice_client
        await server.disconnect()
        
    @commands.command(name='LOL', help = "When someone says some dumb ass take")
    async def playLol(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/LOL.mp3"))
        sleep(5)
        server = ctx.message.guild.voice_client
        await server.disconnect()
        

    @commands.command(name='moan', help = "When someone says some dumb ass take")
    async def playMoan(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/moan.mp3"))
        sleep(6)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='WAA', help = "When someone says some dumb ass take")
    async def playWAA(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/WAA.mp3"))
        sleep(5)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='bruh', help = "When someone says some dumb ass take")
    async def playBruh(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/bruh.mp3"))
        sleep(2)
        server = ctx.message.guild.voice_client
        await server.disconnect()

def setup(bot):
    bot.add_cog(AudioClips(bot))

