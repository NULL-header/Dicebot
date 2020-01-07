# encoding:utf-8
import random
import re


class concentdice(object):
    def ndice(self, rolls: int, limit: int):
        return [self.dice(limit) for r in range(rolls)]

    def dice(self, limit: int):
        return random.randint(1, limit)

    def dice_split(self, rolls: int, limit: int):
        result = "[ "
        n = self.ndice(rolls, limit)
        for i in n:
            result += str(i) + ", "
        result = result[:-2] + " " + "] = "
        sum = 0
        for i in n:
            sum += i
        result += str(sum)
        return result

    def swdice(self):
        from dice_sw import SwDice
        return SwDice()

    def run(self, msg):
        if re.fullmatch(r"\d+d\d+", msg):
            rolls, limit = map(int, msg.split("d"))
            return self.dice_split(rolls, limit)
        if re.search("^ch ", msg):
            return random.choice(msg[3:].split(" "))
        return "a"
