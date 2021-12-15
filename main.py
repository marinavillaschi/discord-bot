import discord
from discord.ext import commands
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print("o bot ta on")

    scheduler = AsyncIOScheduler()

    # horário com 3h a mais para rodar no heroku (timezone UTC)
    scheduler.add_job(job_bater_ponto, CronTrigger(day_of_week = "MON-FRI", hour="23", minute="28", second="0")) 
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


async def job_bater_ponto():
    await client.wait_until_ready()
    c = client.get_channel(918949634259431469)
    await c.send("lembrar de bater ponto!!")


TOKEN = config("token")
client.run(TOKEN)