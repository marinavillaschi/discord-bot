import discord
from discord.ext import commands
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

intents = discord.Intents.default()
intents.members = True 

bot = commands.Bot(command_prefix='/', intents = intents)

# client = discord.Client(intents = intents)


@bot.event
async def on_ready():
    print("o bot ta on")

    # horário com 3h a mais para rodar no heroku (timezone UTC)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(job_bater_ponto, CronTrigger(day_of_week="MON-FRI", hour="12, 15, 16, 21")) 
    scheduler.start()


async def job_bater_ponto():
    await client.wait_until_ready()
    c = client.get_channel(918949634259431469)
    await c.send("Bater ponto!")


@bot.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    mention = message.author.mention

    # prevenir erro dele falar com ele mesmo
    if(message.author.bot):
        return

    # responder ao bom dia
    if(content == "bom dia" or content == "dia"):
        await channel.send("Tenha um ótimo dia " + mention)

    # responder ao morning
    if(content == "good morning" or content == "morning"):
        await channel.send("Have a great day " + mention)


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
async def calculate_expression(ctx, expression):
    expression = "".join(expression)
    response = eval(expression)
    await ctx.send("Resposta = " + str(response))

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)



TOKEN = config("token")
bot.run(TOKEN)