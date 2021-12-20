import discord
from discord.ext import commands
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

intents = discord.Intents.default()
intents.members = True 

bot = commands.Bot(command_prefix='/', intents = intents)

channel_id = config("channel_id")



@bot.event
async def on_ready():
    print("o bot ta on")

    # horário com 3h a mais para rodar no heroku (timezone UTC)
    scheduler = AsyncIOScheduler()
    scheduler.add_job(job_bater_ponto, CronTrigger(day_of_week="MON-FRI", hour="12, 15, 16, 21")) 
    scheduler.start()


async def job_bater_ponto():
    await bot.wait_until_ready()
    c = bot.get_channel(channel_id)
    await c.send("Bater ponto!", delete_after = 3600)


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


TOKEN = config("token")
bot.run(TOKEN)