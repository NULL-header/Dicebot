# encoding:utf-8
import random

from dice import concentdice


class SwDice(concentdice):
    def __init__(self):
        self.dicemode = "sw"

    def dices(self):
        return [random.randint(1, 6), random.randint(1, 6)]
