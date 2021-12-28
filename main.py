import discord
from discord.ext import commands
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from randomPhrases import randomPhrases
from datetime import datetime

intents = discord.Intents.default()
intents.members = True 

bot = commands.Bot(command_prefix='/', intents = intents)

channel_id = config("channel_id")

@bot.event
async def on_ready():
    print("----------------------------\no bot ta on\n----------------------------")

    # horário com 3h a mais para rodar no heroku (timezone UTC)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(job_bater_ponto, CronTrigger(day_of_week="MON-FRI", hour="12, 15, 16, 18, 21"))
    scheduler.start()
    

async def job_bater_ponto():
    await bot.wait_until_ready()
    c = bot.get_channel(int(channel_id))
    if datetime.now().hour == 9:
        await c.send(randomPhrases(), delete_after = 3600)
        await c.send(":white_check_mark:  Não esqueça de bater o ponto! ", delete_after = 3600)
    elif datetime.now().hour == 18:
        await c.send("Hora de bater ponto!\nBom descanso! :wave:  ", delete_after = 3600)
    else:
        await c.send("Bater ponto! ", delete_after = 3600)
    

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

    # responder ao bonjour
    if(content == "bonjour" or content == "salut"):
        await channel.send("Salut " + mention)

    # teste do ponto
    if(content == "ponto"):
        await job_bater_ponto()


TOKEN = config("token")
bot.run(TOKEN)