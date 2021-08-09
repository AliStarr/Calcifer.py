import discord
import logging, os, os.path, random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info("Games Cog loaded")
        print('Games Cog loaded')
    
    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be NdN! E.g: 1d6 rolls a 6 sided die once.')
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
    
    @commands.command(name='8ball')
    async def eight_ball(self, ctx, *, msg):
        '''Ask the magic 8ball a question'''
        
        answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes","Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again","Don't count on it", "My reply is no", "My sources say no", "Outlook not so good","Very doubtful"]
        result = random.randint(1, len(answers))

        try:

            embed = discord.Embed(title=f"Magic 8 Ball")
            embed.add_field(name='\u200b', value=f'**{ctx.author}** shakes the magic 8 ball and asks: {msg}') # ZWS to get around needing a name.
            embed.add_field(name='\u200b', value=f'**The magic 8 ball responds**: {answers[result]}', inline=False)

            await ctx.send(embed=embed)
        except Exception as err:
            print(err)
       

        

def setup(bot):
    bot.add_cog(Games(bot))