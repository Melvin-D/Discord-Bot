import discord
import os
from discord.ext import commands
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


op = webdriver.ChromeOptions()
op.add_argument('headless')
op.add_argument("--window-size=1240,800")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=op)

class AramBuilds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='build', help = "Search for ARAM builds in League of Legends")
    async def screenshotsite(self, ctx, screenquery:str):
        driver.get(f'https://murderbridge.com/Champion/{screenquery}')
        sleep(.5)
        driver.save_screenshot(f"{str(screenquery)}.png")
        embed = discord.Embed(title=f"Build for {screenquery.capitalize()}", description="", color=0x0000FF)
        file = discord.File((f"{screenquery}.png"), filename=str(screenquery) + ".png")
        embed.set_image(url=f"attachment://{screenquery}.png")
        await ctx.send(file=file, embed=embed)
        os.remove(f"C:/Users/Melvin/Desktop/Discord Python Bot/{screenquery}.png")

def setup(bot):
    bot.add_cog(AramBuilds(bot))
