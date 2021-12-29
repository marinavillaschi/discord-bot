from discord.ext import commands
from datetime import datetime
from randomPhrases import randomPhrases
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


class Ponto(commands.Cog):
    """
    Trabalha com lembretes para bater ponto
    """
    def __init__(self, bot):
        self.bot = bot


    # bot.event ==> commands.Cog.listener()
    @commands.Cog.listener()
    async def on_ready(self):
        scheduler = AsyncIOScheduler()
        scheduler.add_job(self.job_bater_ponto, CronTrigger(day_of_week="MON-FRI", hour="12, 15, 16, 21"))
        scheduler.start()


    async def job_bater_ponto(self):
        await self.bot.wait_until_ready()
        c = self.bot.get_channel(int(self.bot.ponto_channel_id))
        if datetime.now().hour == 12:
            await c.send(randomPhrases(), delete_after = 3600)
            await c.send(":white_check_mark:  Não esqueça de bater o ponto! ", delete_after = 3600)
        elif datetime.now().hour == 21:
            await c.send("Hora de bater ponto!\nBom descanso! :wave:  ", delete_after = 3600)
        else:
            await c.send("Bater ponto! ", delete_after = 3600)


def setup(bot):
    bot.add_cog(Ponto(bot))

