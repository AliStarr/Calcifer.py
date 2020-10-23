import discord
import os, os.path, dotenv, random, logging
from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
cwd = os.getcwd()
logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s: %(message)s', datefmt='%d/%m/%y %I:%M:%S %p')

# Bot stuff
description = '''A python remake of Calcifer, my C# discord bot.'''
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='~', description=description, intents=intents)

# Grab all the Cogs
for filename in os.listdir(f'{cwd}\\Cogs'):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    logging.info('Login Started')
    print('Logged in as {bot.user.name} UID: {bot.user.id}.')
    logging.info('Login Completed')
    print('--------')
    await bot.change_presence(activity=discord.Game(name='Version 0.1, now running on Python!'))

# Listen for command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass # Fail silently

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You seem to be missing an argument for the command {ctx.command}. Please try again.')
    
bot.run(TOKEN)
