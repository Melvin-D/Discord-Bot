# bot.py
# Author: Melvin Dharan


import os
import wikipediaapi
import discord
import youtube_dl
import aiohttp
import io
import asyncio
from discord.ext import commands
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from discord.utils import get
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime

#Loads unique bot ID from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


#Declarations for Google Drive directory
gauth = GoogleAuth()
gauth.LoadCredentialsFile("creds.txt")
if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()
drive = GoogleDrive(gauth)
gauth.SaveCredentialsFile("creds.txt")

#Bot will only listen to commands starting with the prefix
bot = commands.Bot(command_prefix='!')

now = datetime.now()


#When bot starts, check if it's connected to any servers and list members in server
@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(f'{bot.user.name} has connected to Discords!')
    print(
        f'{bot.user.name} is connected to the following server(s):\n'
        f'{guild.name}(id: {guild.id}')
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="server chat"))

    members = '\n - ' .join([member.name for member in guild.members])
    print (f'Server Members: \n - {members}')
    print(discord.__version__)
    

#Google drive commands
@bot.command(name='upload')
async def uploadfile(ctx):
    file1 = drive.CreateFile({'title': 'Hello.txt'})
    file1.SetContentString('This is a test')
    file1.Upload()

@bot.command(name='upload2')
async def uploadfile(ctx):
    file1 = drive.CreateFile({'parents': [{'id': '1-cPsFS2glQJdUwIySF04HYUrxvrTedo5'}]})
    file1.SetContentString('This is a test')
    file1.Upload()
    
    
#Search Wikipedia for an article
@bot.command(name='wiki', help = "Search wikipedia")
async def wikisummary(ctx, wikiquery: str):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(wikiquery)
    await ctx.send(page_py.summary[0:300])

#Reloads a specific cog for hot-reloading functions without needing to restart entire bot
@bot.command(name='reload')
async def reload(ctx, cog: str):
        try: 
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py') and not filename.startswith("_"):
                    bot.unload_extension(f'cogs.{filename[:-3]}')
                    bot.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
            await ctx.send("Couldnt reload")
            return
        await ctx.send("Successfully reloaded")


#Scans file system for all cogs in directory and loads them
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)




# @bot.command(name='test')
# async def test_test(ctx):
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://cdn.discordapp.com/attachments/556243228555345927/741449535821316137/32kgOWP.png') as resp:
#             if resp.status != 200:
#                 return await ctx.send('Could not download file')
#             data = io.BytesIO(await resp.read())
#             await ctx.send(file=discord.File(data, 'cool_image.png'))
    
#     file1 = drive.CreateFile({'title': f"{ctx.author}  {now}", 'parents': [{'id': '1-cPsFS2glQJdUwIySF04HYUrxvrTedo5'}], 'mimeType': 'image/jpeg'})
#     file1.
#     file1.Upload()



# # pic_ext = ['.jpg', '.png', '.jpeg']
# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#          return

#     if message.attachments:
#         await message.channel.send("Good")        
#         await message.channel.send(message.attachments[0].url)
#     else:
#         await message.channel.send("SEEN")

#     # for extentions in pic_ext:
#     #     if extentions in message.content:
#     #         file1 = drive.CreateFile({'title': f"{message.author}  {now}", 'parents': [{'id': '1-cPsFS2glQJdUwIySF04HYUrxvrTedo5'}], 'mimeType': 'image/jpeg'})
#     #         file1.SetContentFile('gio.png')
#     #         file1.Upload()
#     await bot.process_commands(message)
