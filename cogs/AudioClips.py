import discord
import asyncio
import os
from discord.ext import commands
from discord import FFmpegPCMAudio

class AudioClips(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def checkUser(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return None
        
        path = f'C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/{ctx.message.content[1:]}.mp3'
        if os.path.isfile(path) == False:
            await ctx.send(f"{ctx.author.emtion} Not a valid command")
            return
        # voice.play(FFmpegPCMAudio(f"C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/{ctx.message.content[1:]}.mp3"))

        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio(path))
        await asyncio.sleep(1.3)  
        server = ctx.message.guild.voice_client
        await server.disconnect()
        
    @commands.command(name='SUB', help = "When someone says some dumb ass take")
    async def playTheRockSUB(self, ctx):
        await self.checkUser(ctx)
        # await asyncio.sleep(1.3)

    @commands.command(name='WAA2', help = "GOLDEN")
    async def playWAA2(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            await ctx.send(name)
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/WAA2.mp3"))
        await ctx.send("<:PogUbc:744507472404021300>")
        await asyncio.sleep(3.4)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='BABY', help = "baa baa boo boo baby ass")
    async def playBABY(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            await ctx.send(name)
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/Crybaby.mp3"))
        await asyncio.sleep(2)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='door', help = "knock knock")
    async def playDoor(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            await ctx.send(name)
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/binaural.mp3"))
        await asyncio.sleep(4)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='DEEZ', help = "you from sugondese?")
    async def playDEEZ(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/DEEZ.mp3"))
        await asyncio.sleep(2.7)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='stopcomplaining', help = "I aint ur daddy")
    async def playSoulja(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/stopcomplaininglikesomehoes.mp3"))
        await asyncio.sleep(5.4)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='GotThat', help = "help me")
    async def playIRONY(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/IGotThat.mp3"))
        await asyncio.sleep(2.7)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='GotThatGolden', help = "help me")
    async def playGOLDEN(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/GotThatGolden.mp3"))
        await asyncio.sleep(3.2)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='AsianPeople', help = "help me")
    async def palyAsianPeople(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/AsianPeopleGOLD.mp3"))
        await asyncio.sleep(6.4)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='guh', help = "-$50k")
    async def playGuh(self, ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/guh.mp3"))
        await ctx.send("<:guh:647989815085891584>")
        await asyncio.sleep(1.0)
        server = ctx.message.guild.voice_client
        await server.disconnect()
        
    @commands.command(name='LOL', help = "HAHA")
    async def playLol(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/LOL.mp3"))
        await asyncio.sleep(5)
        server = ctx.message.guild.voice_client
        await server.disconnect()
        

    @commands.command(name='moan', help = "nut")
    async def playMoan(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/moan.mp3"))
        await asyncio.sleep(6)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='WAA', help = "WAAA GOLDEN")
    async def playWAA(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/WAA.mp3"))
        await asyncio.sleep(5)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='bruh', help = "epic moment")
    async def playBruh(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/bruh.mp3"))
        await asyncio.sleep(2)
        server = ctx.message.guild.voice_client
        await server.disconnect()

    @commands.command(name='matt', help = "bapcsalescanada")
    async def playMatt(self,ctx):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return
        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio("C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/matt.mp3"))
        await asyncio.sleep(4)
        server = ctx.message.guild.voice_client
        await server.disconnect()

def setup(bot):
    bot.add_cog(AudioClips(bot))

