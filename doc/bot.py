# encoding:utf-8

from discord.ext import commands


class MyBot(commands.Bot):
    def __init__(self, dict_keys: dict, prfix: str):
        super().__init__(prfix)
        self.dict_keys = dict_keys
        self.load_extension("cog")

    async def on_ready(self):
        print("logged in as {}".format(self.user))

    def wake(self):
        self.run(self.dict_keys["token"])
