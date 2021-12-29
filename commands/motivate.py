from discord.ext import commands
from randomPhrases import randomPhrases


class Motivate(commands.Cog):
    """
    Trabalha com frases motivacionais
    """
    def __init__(self, bot):
        self.bot = bot


    # bot.command ==> commands.command()
    @commands.command()
    async def motivate(self, ctx):
        """
        Traz uma frase motivacional. Argumento: não requer.
        """
        await ctx.send(randomPhrases())

    

def setup(bot):
    bot.add_cog(Motivate(bot))

