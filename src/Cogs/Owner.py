import discord
import logging, os, os.path, random, sys
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        logging.info('Owner Cog loaded')

    @commands.command()
    @commands.is_owner()
    async def quit(self, ctx):
        """Kills the bot"""
        await ctx.send('Bye!')
        logging.info('Bot exit requested')
        sys.exit(0) # VSCode hates not having an arg here. Raises an exception. Pass 0 for a clean exit.
    
    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        """Restrat the bot"""
        try:
            await ctx.send('Restarting...')
            logging.info('Bot restart requested')
            os.execl(sys.executable, sys.executable, *sys.argv) # Restart the process with the same arguments
        except Exception as err:
            print(f'Exception thrown trying to restart bot {err}')
            logging.error(f'Exception thrown trying to restart bot {err}')
        


def setup(bot):
    bot.add_cog(Owner(bot))
