import discord
import os, os.path, dotenv, random, logging
from discord.ext import commands

dotenv.load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
cwd = os.getcwd()
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s: %(message)s', datefmt='%d/%m/%y %I:%M:%S %p')

BOT_VERSION = os.getenv("VERSION")

# Bot stuff
description = '''A python remake of Calcifer, my C# discord bot.'''
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents, case_insesnsitive=True)

# Grab all the Cogs
for filename in os.listdir(f"{cwd}//src//Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")

@bot.event
async def on_ready():
    logging.info('Login Started')
    print(f'Logged in as {bot.user.name}. UID: {bot.user.id}.')
    logging.info('Login Completed')
    print('--------')
    await bot.change_presence(activity=discord.Game(name=f'Version {BOT_VERSION}'))

# Listen for command errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass # Fail silently

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'You seem to be missing an argument for the command {ctx.command}. Please try again.')
    
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send('Command Invoke Error. Something fucked up.')
        logging.error(f'Command Invoke Error in command {ctx.command}!')
    
    if isinstance(error, commands.DisabledCommand):
        await ctx.send(f'The {ctx.command} command has been disabled.')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'You dont have permission to run {ctx.command}!')
    
bot.run(TOKEN)
