import discord
from discord.ext import commands
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
# from discord_slash import SlashCommand, SlashContext


intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print("o bot ta on")

    scheduler = AsyncIOScheduler()

    # horário com 3h a mais para rodar no heroku (timezone UTC)
    scheduler.add_job(job_bater_ponto_1, CronTrigger(hour="12, 15, 16, 21", minute="15", second="0")) 
    scheduler.start()


# slash = SlashCommand(client)

# @slash.slash(name="test")
# async def test(ctx: SlashContext):
#     embed = discord.Embed(title="Embed Test")
#     await ctx.send(embed=embed)




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
        await channel.send(datetime.now())


async def job_bater_ponto_1():
    await client.wait_until_ready()
    c = client.get_channel(918949634259431469)
    await c.send("Bater ponto!")
    await c.send(datetime.now())


TOKEN = config("token")
client.run(TOKEN)