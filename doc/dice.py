# encoding:utf-8
import random
import re


class concentdice(object):
    def __init__(self):
        self.dicemode = "normal"
        self.dicemodelist = ["normal", "sw"]

    def ndice(self, rolls: int, limit: int):
        if (not isinstance(rolls, int)) or rolls <= 0:
            return None
        dices = [self.dice(limit) for r in range(rolls)]
        if None in dices:
            return None
        return dices

    def dice(self, limit: int):
        if (not isinstance(limit, int)) or limit <= 0:
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
        if not isinstance(msg, str):
            return None
        if re.fullmatch(r"\d+d\d+", msg):
            rolls, limit = map(int, msg.split("d"))
            return self.dice_split(rolls, limit)
        if re.search("^ch ", msg):
            return self.choice(msg[3:].split(" "))
        return None

    def choice_random(self, args):
        if not isinstance(args, list) or not args:
            return None
        for i in args:
            if not isinstance(i, str):
                return None
        return random.choice(args)

    def choice(self, args):
        arg_random = self.choice_random(args)
        if not arg_random:
            return None
        result = "[ "
        for i in args:
            result += i + ", "
        result = result[:-2] + " ] = " + arg_random
        return result

    def set_dice(self, dice: str):
        if dice in self.dicemodelist:
            self.dicemode = dice

    def wake(self, msg):
        if self.dicemode == "normal":
            dice = self
        return dice.run(msg)
