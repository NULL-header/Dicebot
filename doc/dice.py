# encoding:utf-8
import random


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
        return True
