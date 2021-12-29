import discord
from discord.ext import commands
from decouple import config

intents = discord.Intents.default()
intents.members = True 

bot = commands.Bot(command_prefix='/', intents = intents)

channel_id = config("channel_id")
bot.ponto_channel_id = channel_id

cogs = ['manager',
        'tasks.ponto',
        'commands.calc',
        'commands.info',
        'commands.motivate',]

def load_cogs(bot):
    for cog in cogs:
        bot.load_extension(cog)

load_cogs(bot)

TOKEN = config("token")
bot.run(TOKEN)