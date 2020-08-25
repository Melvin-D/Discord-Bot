import discord
import asyncio
import os
from discord.ext import commands
from discord import FFmpegPCMAudio

class AudioClips(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def checkUser(self, ctx, sleepTime):
        if ctx.author.voice is None:
            await ctx.send(f"{ctx.author.mention} You need to be in a voice channel to do that")
            return None
        
        path = f"C:/Users/Melvin/Desktop/Discord Python Bot/AudioClips/{ctx.message.content[1:]}.mp3"
        if os.path.isfile(path) == False:
            await ctx.send(f"{ctx.author.mention} Not a valid command")
            return

        channel = ctx.author.voice.channel
        voice = await channel.connect()
        voice.play(FFmpegPCMAudio(path))
        await asyncio.sleep(sleepTime)  
        server = ctx.message.guild.voice_client
        await server.disconnect()

        
    @commands.command(name='SUB', help = "The Rock")
    async def playTheRockSUB(self, ctx):
        sleepTime = 1.3
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='WAA2', help = "Golden")
    async def playWAA2(self, ctx):
        sleepTime = 3.6
        await ctx.send("<:PogUbc:744507472404021300>")
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='BABY', help = "Crying")
    async def playBABY(self, ctx):
        sleepTime = 2
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='door', help = "Knock")
    async def playDoor(self, ctx):    
        sleepTime = 4   
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='DEEZ', help = "Deez")
    async def playDEEZ(self, ctx):
        sleepTime = 2.7
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='stopcomplaining', help = "Aint your")
    async def playSoulja(self, ctx):
        sleepTime = 5.4
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='GotThat', help = "Ironic")
    async def playIRONY(self, ctx):
        sleepTime = 2.7
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='GotThatGolden', help = "Remix")
    async def playGOLDEN(self, ctx):
        sleepTime = 3.2
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='AsianPeople', help = "Remix2")
    async def palyAsianPeople(self, ctx):
        sleepTime = 6.4
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='guh', help = "-$50k")
    async def playGuh(self, ctx):
        sleepTime = 1
        await ctx.send("<:guh:647989815085891584>")
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='LOL', help = "Laugh")
    async def playLol(self,ctx):
        sleepTime = 5
        await self.checkUser(ctx, sleepTime) 

    @commands.command(name='YOO', help = "YOO")
    async def playYOO(self,ctx):
        sleepTime = 2.8
        await self.checkUser(ctx, sleepTime) 

    @commands.command(name='ASMR', help = "asmr")
    async def playASMR(self,ctx):
        sleepTime = 6.9
        await ctx.send("<:EatTheTestie:708235731700547605>")
        await self.checkUser(ctx, sleepTime) 

    @commands.command(name='ASMReact', help = "asmract")
    async def playASMReact(self,ctx):
        sleepTime = 5
        await self.checkUser(ctx, sleepTime) 

    @commands.command(name='bass', help = "BBBBBBB")
    async def playBass(self,ctx):
        sleepTime = 1.5
        await self.checkUser(ctx, sleepTime) 

    @commands.command(name='moan', help = "Moan")
    async def playMoan(self,ctx):
        sleepTime = 6
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='WAA', help = "Waa Golden")
    async def playWAA(self,ctx):
        sleepTime = 5
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='bruh', help = "Epic")
    async def playBruh(self,ctx):
        sleepTime = 2
        await self.checkUser(ctx, sleepTime)
    
    @commands.command(name='bruhH', help = "EpicH")
    async def playBruhH(self,ctx):
        sleepTime = 1.5
        await self.checkUser(ctx, sleepTime)

    @commands.command(name='matt', help = "bapcsalescanada")
    async def playMatt(self,ctx):
        sleepTime = 4
        await self.checkUser(ctx, sleepTime)


def setup(bot):
    bot.add_cog(AudioClips(bot))

