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
    scheduler.add_job(job_bater_ponto_1, CronTrigger(day_of_week = "MON-FRI", hour="13", minute="38", second="0")) 
    scheduler.add_job(job_bater_ponto_2, CronTrigger(day_of_week = "MON-FRI", hour="14", minute="38", second="0")) 
    scheduler.add_job(job_bater_ponto_3, CronTrigger(day_of_week = "MON-FRI", hour="15", minute="38", second="0")) 
    scheduler.add_job(job_bater_ponto_4, CronTrigger(day_of_week = "MON-FRI", hour="16", minute="38", second="0")) 
    scheduler.add_job(job_bater_ponto_5, CronTrigger(day_of_week = "MON-FRI", hour="17", minute="38", second="0")) 
    scheduler.add_job(job_bater_ponto_6, CronTrigger(day_of_week = "MON-FRI", hour="18", minute="38", second="0")) 
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

async def job_bater_ponto_2():
    await client.wait_until_ready()
    c = client.get_channel(918949634259431469)
    await c.send("teste 2")

async def job_bater_ponto_3():
    await client.wait_until_ready()
    c = client.get_channel(918949634259431469)
    await c.send("teste 3")

async def job_bater_ponto_4():
    await client.wait_until_ready()
    c = client.get_channel(918949634259431469)
    await c.send("teste 4")

async def job_bater_ponto_5():
    await client.wait_until_ready()
    c = client.get_channel(918949634259431469)
    await c.send("teste 5")

async def job_bater_ponto_6():
    await client.wait_until_ready()
    c = client.get_channel(918949634259431469)
    await c.send("teste 6")


TOKEN = config("token")
client.run(TOKEN)