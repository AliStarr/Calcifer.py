import discord
import logging, os, os.path, random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Games Cog loaded")
    
    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be NdN!')
            return
            
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command()
    async def flip(self, ctx):
        """Flips a coin. Heads or tails"""
        flip = random.randint(0, 1) # Unlike C# the max rage is NOT exclusive
        if flip == 0:
            await ctx.send(f'Heads!')
        else:
            await ctx.send(f'Tails!')
        

def setup(bot):
    bot.add_cog(Games(bot))