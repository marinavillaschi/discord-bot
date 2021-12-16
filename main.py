import discord
from decouple import config
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
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

    # responder ao oi
    if(content == "oi" + mention or content == "ola" or content == "olá"):
        await channel.send("Tenha um ótimo dia " + mention)

    # responder ao bom dia
    if(content == "bom dia" or content == "dia"):
        await channel.send("Tenha um ótimo dia " + mention)

    # responder ao morning
    if(content == "good morning" or content == "morning"):
        await channel.send("Have a great day " + mention)


async def job_bater_ponto_1():
    await client.wait_until_ready()
    c = client.get_channel(918949634259431469)
    await c.send("Bater ponto!")


TOKEN = config("token")
client.run(TOKEN)