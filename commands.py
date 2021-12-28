import discord
from discord.ext import commands
from decouple import config
from randomPhrases import randomPhrases

bot = commands.Bot(command_prefix='/')

@bot.command()
async def info(ctx):
    """
    Mostra as habilidades do bot. Argumento: não requer.
    """
    embed = discord.Embed(
        title="Olá! Eu sou o novo estagiário da Qesh!",
        description="Aqui vai uma lista das coisas que posso fazer para você:",
        color=discord.Colour.blue()
        )

    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)

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

@bot.command(name="calc")
async def calculate_expression(ctx, *expression):
    """
    Calcula uma expressão matemática simples. Argumento: expressão.
    """
    expression = ' '.join(expression)
    response = eval(expression)
    await ctx.send("Resposta = " + str(response))


@bot.command()
async def motivate(ctx):
    """
    Traz uma frase motivacional. Argumento: não requer.
    """
    await ctx.send(randomPhrases())

TOKEN = config("token")
bot.run(TOKEN)