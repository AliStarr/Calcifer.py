import discord
import logging, os, os.path, random, platform, psutil, humanfriendly
from discord.ext import commands


class Public(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Public Cog loaded')
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
        pid = os.getpid()
        memory_use = psutil.Process(pid).memory_info().rss
        embed = discord.Embed(title=f'Calcifer Bot Information')
        embed.add_field(name='**General**', value=f"Author: `{app_info.owner}`\nVersion: `{version}`\nGithub: `https://github.com/AliStarr/Calcifer.py`")
        embed.add_field(name='System Information', value=f"Python Version: `{platform.python_version()}`\nDiscord.py Version: `{discord.__version__}`\n Memory Usage: `{humanfriendly.format_size(memory_use)}`")
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, msg: str):
        """Echos the input"""
        if msg.startswith('/'):
            await ctx.send('Nice try.') # dont allow commands to be run
        await ctx.send('\u200b{msg}') # add a zero white space so we don't trigger bots.

    @commands.command()
    async def joined(self, ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send(f'{member.name} Joined at {member.joined_at}')

    @commands.command()
    async def ping(self, ctx):
        """Get round trip information"""
        await ctx.send(f'Pong! ``{round(self.bot.latency * 1000)}ms``')

    @commands.command()
    async def bug(self, ctx):
        await ctx.send(f"Pinging Alister and to tell him he sucks at programming... <@181766490050002945>") # I'll figure out how to mention owner_id later


def setup(bot):
    bot.add_cog(Public(bot))