# encoding:utf-8

from dice import *
from discord.ext import commands


class Cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        text = ""
        if msg.author.bot:
            return
        text += msg.author.mention + "\n"
        try:
            rolls, limit = map(int, msg.content.split("d"))
            text += concentdice.dice_split(rolls, limit)
        finally:
            pass
        await msg.channel.send(text)


def setup(bot):
    bot.add_cog(Cmds(bot))
