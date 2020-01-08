# encoding:utf-8
import random

from dice import concentdice


class SwDice(concentdice):
    def swdice(self):
        return [random.randint(1, 6), random.randint(1, 6)]
