from discord.ext import commands
from tasks.ponto import Ponto

class Manager(commands.Cog):
    """
    Gerencia o bot
    """
    def __init__(self, bot):
        self.bot = bot
        self.ponto = Ponto(bot)

    
    # bot.event ==> commands.Cog.listener()
    @commands.Cog.listener()
    async def on_ready(self):
        print("----------------------------\no bot ta on\n----------------------------")


    # bot.event ==> commands.Cog.listener()
    @commands.Cog.listener()
    async def on_message(self, message):
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
            await self.ponto.job_bater_ponto()


def setup(bot):
    bot.add_cog(Manager(bot))