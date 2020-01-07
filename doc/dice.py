# encoding:utf-8
import random


class concentdice(object):
    def ndice(rolls: int, limit: int):
        return [dice(limit) for r in range(rolls)]

    def dice(limit: int):
        return random.randint(1, limit)

    def dice_split(rolls: int, limit: int):
        result = "[ "
        n = ndice(rolls, limit)
        for i in n:
            result += str(i) + ", "
            result += "] = "
        sum = 0
        for i in n:
            sum += i
        result += str(sum)
        return result
