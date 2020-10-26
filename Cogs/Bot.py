import discord
import logging, os, os.path, random
from discord.ext import commands

class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Bot Cog loaded")


def setup(bot):
    bot.add_cog(Bot(bot))