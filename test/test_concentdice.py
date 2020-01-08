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
        d6 = self.d.dice(-1)
        self.assertEqual(None, d6)

    def test_ndice(self):
        for i in range(100):
            d6s = self.d.ndice(3, 6)
            for j in d6s:
                result = 1 <= j and j <= 6
                self.assertTrue(result)
        d6s = self.d.ndice(-1, 1)
        self.assertEqual(d6s, None)
        d6s = self.d.ndice(1, -1)
        self.assertEqual(d6s, None)
        d6s = self.d.ndice(-1, -1)
        self.assertEqual(d6s, None)

    def test_dice_split(self):
        for i in range(100):
            strd6s = self.d.dice_split(3, 6)
            check = r"\[ \d+, \d+, \d+ \] = \d+"
            result = bool(re.fullmatch(check, strd6s))
            self.assertTrue(result)
        strd6s = self.d.dice_split(-1, 1)
        self.assertEqual(None, strd6s)
        strd6s = self.d.dice_split(1, -1)
        self.assertEqual(None, strd6s)
        strd6s = self.d.dice_split(-1, -1)
        self.assertEqual(None, strd6s)

    def test_swdice(self):
        swd = self.d.swdice()
        d6s = swd.swdice()
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
            check = r"[abc]"
            result = bool(re.fullmatch(check, strd6s))
            self.assertTrue(result)

    def test_set_dice(self):
        strd6s = self.d.set_dice("normal")
        self.assertEqual("normal", self.d.dice)

    def test_wake(self):
        dice = concentdice()
        dice.set_dice("normal")
        strd6s = dice.wake("2d6")

    def test_(self):
        pass

    def tearDown(self):
        pass
