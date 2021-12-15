import discord
from discord.ext import commands
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import date



intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print("o bot ta on")

    scheduler = AsyncIOScheduler()

    # horário com 3h a mais para rodar no heroku (timezone UTC)
    scheduler.add_job(job_bater_ponto_1, CronTrigger(hour="1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23", minute="20, 22, 24", second="0")) 
    scheduler.start()


@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    mention = message.author.mention

    # prevenir erro dele falar com ele mesmo
    if(message.author.bot):
        return

    # responder ao bom dia
    if(content == "bom dia"):
        await channel.send("bom dia " + mention)


async def job_bater_ponto_1():
    await client.wait_until_ready()
    c = client.get_channel(918949634259431469)
    await c.send("teste 1")
    await c.sent(date.today())


TOKEN = config("token")
client.run(TOKEN)