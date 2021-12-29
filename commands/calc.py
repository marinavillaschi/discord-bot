from discord.ext import commands


class Calc(commands.Cog):
    """
    Trabalha com expressões matemáticas simples
    """
    def __init__(self, bot):
        self.bot = bot

    # bot.command ==> commands.command()
    @commands.command(name="calc")
    async def calculate_expression(self, ctx, *expression):
        """
        Calcula uma expressão matemática simples. Argumento: expressão.
        """
        expression = ' '.join(expression)
        response = eval(expression)
        await ctx.send("Resposta = " + str(response))


def setup(bot):
    bot.add_cog(Calc(bot))

