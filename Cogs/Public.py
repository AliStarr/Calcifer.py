import discord
import logging, os, os.path, random
from discord.ext import commands
from discord.utils import get

class Public(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Public Cog loaded")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return # Don't reply to our selves.
    
    @commands.command()
    async def info(self, ctx):
        """Displays bot information"""
        app_info = await self.bot.application_info()
        version = os.getenv("VERSION")
        embed = discord.Embed(title=f'Calcifer Bot Information')
        embed.add_field(name='**General**', value=f"Author: `{app_info.owner}`\nVersion: {version}")
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, msg: str):
        """Echos the input"""
        if msg.startswith('~'):
            await ctx.send('Nice try.') # dont allow commands to be run
        await ctx.send('\u200b{msg}') # add a zero white space so we don't trigger bots.

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
    async def joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send('{0.name} Joined in {0.joined_at}'.format(member))

    @commands.command()
    async def Ping(self, ctx):
        await ctx.send(f'Pong! ``{round(self.bot.latency * 1000)}ms``')

def setup(bot):
    bot.add_cog(Public(bot))