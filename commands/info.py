import discord
from discord.ext import commands


class Info(commands.Cog):
    """
    Mostra as habilidades do bot
    """
    def __init__(self, bot):
        self.bot = bot


    # bot.command ==> commands.command()
    @commands.command()
    async def info(self, ctx):
        """
        Mostra as habilidades do bot. Argumento: não requer.
        """
        embed = discord.Embed(
            title="Olá! Eu sou o novo estagiário da Qesh!",
            description="Aqui vai uma lista das coisas que posso fazer para você:",
            color=discord.Colour.blue()
            )

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.add_field(
            name='/calc   :abacus:',
            value='Eu calculo uma expressão matemática simples. Argumento: expressão.\n',
            inline=False
        )

        embed.add_field(
            name='/motivate   :thinking:',
            value='Eu te digo uma frase motivacional. Argumento: não requer.\n',
            inline=False
        )

        embed.add_field(
            name=':alarm_clock: Lembrete para bater o ponto',
            value='Eu passo pra te lembrar de bater o ponto!',
            inline=False
        )

        await ctx.send(embed=embed)

    

def setup(bot):
    bot.add_cog(Info(bot))

