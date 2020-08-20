# bot.py

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
from discord.ext import commands
from discord.utils import get
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


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


bot = commands.Bot(command_prefix='!')


now = datetime.now()


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(f'{bot.user.name} has connected to Discords!')
    print(
        f'{bot.user.name} is connected to the following server(s):\n'
        f'{guild.name}(id: {guild.id}')
    
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="pebnis hahha"))

    members = '\n - ' .join([member.name for member in guild.members])
    print (f'Server Members: \n - {members}')
    print(discord.__version__)
    

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
    
    

@bot.command(name='wiki', help = "Search wikipedia")
async def wikisummary(ctx, wikiquery: str):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(wikiquery)
    await ctx.send(page_py.summary[0:300])

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

# @bot.event      
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     birthday_greetings = ['bbday' , 'haha']


#     ***REMOVED*** = ['***REMOVED***']
#     ***REMOVED*** = ['***REMOVED***', '***REMOVED***']
#     for information in ***REMOVED***:
#         if information in message.content:
#             await message.channel.send("Please ***REMOVED*** " + str(message.author.mention))
#     for information in ***REMOVED***:
#         if information in message.content:
#             await message.channel.send("Please ***REMOVED*** " + str(message.author.mention))
# bot.counter = {}
# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return
#     ***REMOVED*** = ['***REMOVED***', '***REMOVED***']
#     ***REMOVED*** = '***REMOVED***'
#     author = message.author.id

#     if author not in bot.counter:
#         bot.counter[author] = 0

    

#     for information in ***REMOVED***:
#         if information in message.content:
#             await message.channel.send(f"{message.author.mention} +1")
#             bot.counter[author] += 1
#     await bot.process_commands(message)
