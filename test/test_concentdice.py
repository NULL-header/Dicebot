# coding:utf-8
import re
import unittest

try:
    from dice import concentdice
finally:
    pass


class TestConcentDice(unittest.TestCase):
    def setUp(self):
        self.d = concentdice()

    def test_dice(self):
        for i in range(100):
            d6 = self.d.dice(6)
            result = 1 <= d6 and d6 <= 6
            self.assertTrue(result)

    def test_ndice(self):
        for i in range(100):
            d6s = self.d.ndice(3, 6)
            for j in d6s:
                result = 1 <= j and j <= 6
                self.assertTrue(result)

    def test_dice_split(self):
        for i in range(100):
            strd6s = self.d.dice_split(3, 6)
            check = r"\[ \d+, \d+, \d+ \] = \d+"
            result = bool(re.fullmatch(check, strd6s))
            self.assertTrue(result)

    def test_swdice(self):
        swd = self.d.swdice()
        for i in range(100):
            d6s = swd.dice()
            result = d6s is not None
            self.assertTrue(result)

    def test_run_dice_split(self):
        for i in range(100):
            strd6s = self.d.run("2d6")
            check = r"\[ \d+, \d+ \] = \d+"
            result = bool(re.fullmatch(check, strd6s))
            self.assertTrue(result)

    def test_run_choice(self):
        for i in range(100):
            strd6s = self.d.run("ch a b c")
            check = r"\[abc\]"
            result = bool(re.fullmatch(check, strd6s))
            self.assertTrue(result)

    def test_(self):
        pass

    def tearDown(self):
        pass
