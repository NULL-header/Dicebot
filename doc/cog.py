# encoding:utf-8

from dice import *
from discord.ext import commands


class Cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot:
            return
        try:
            rolls, limit = map(int, msg.content.split("d"))
            await msg.channel.send(dice_split(rolls, limit))
        finally:
            pass


def setup(bot):
    bot.add_cog(Cmds(bot))
