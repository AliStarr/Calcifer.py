import discord
from discord.ext import commands
import random

description = '''A python remake of Calcifer, my C# discord bot.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='~', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as ')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')

@bot.command()
async def add(ctx, left: int, right: int):
    """adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be NdN!')
            return
        
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

@bot.command()
async def joined(ctx, memberL discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} Joined in {0.joined_at}'.format(member))

bot.run('token')
