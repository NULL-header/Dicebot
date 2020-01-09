# encoding:utf-8
import random
import re


class concentdice(object):
    def __init__(self):
        self.dicemode = "normal"

    def ndice(self, rolls: int, limit: int):
        if (not isinstance(rolls, int)) or rolls < 0:
            return None
        dices = [self.dice(limit) for r in range(rolls)]
        if None in dices:
            return None
        return dices

    def dice(self, limit: int):
        if (not isinstance(limit, int)) or limit < 0:
            return None
        return random.randint(1, limit)

    def dice_split(self, rolls: int, limit: int):
        result = "[ "
        n = self.ndice(rolls, limit)
        if not n:
            return None
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
            return self.choice(msg[3:].split(" "))

    def choice(self, args):
        return random.choice(args)

    def set_dice(self, dice: str):
        self.dicemode = dice

    def wake(self, msg):
        if self.dicemode == "normal":
            dice = self
        return dice.run(msg)
