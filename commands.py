import discord
from discord.ext import commands
from decouple import config

bot = commands.Bot(command_prefix='/')

@bot.command()
async def info(ctx):
    """
    /info
    """
    embed = discord.Embed(
        title="Olá! Eu sou o novo estagiário da Qesh!",
        description="Aqui vai uma lista das coisas que posso fazer para você:",
        color=discord.Colour.blue()
        )

    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)

    embed.add_field(
        name='/calc   :abacus:',
        value='Eu faço operações matemáticas simples.\n',
        inline=False
    )

    embed.add_field(
        name='/test   :test_tube:',
        value='Eu só repito o argumento, é uma função de teste.\n',
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
    expression = ' '.join(expression)
    response = eval(expression)
    await ctx.send("Resposta = " + str(response))


# import disnake
# from disnake.ext import commands

# @bot.slash_command(description="Multiplies the number by 7")
# async def multiply(inter, number: int):
#     await inter.response.send_message(number * 7)


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

TOKEN = config("token")
bot.run(TOKEN)