import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

description = '''Dungeons & Dragons dice rolling bot.'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # chagnes bot 'Playing' status
    await bot.change_presence(activity=discord.Game(name='!help for more info'))
    print('Successfully booted and logged in...!')

bot.run(TOKEN)