# coding:utf-8

import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..\\doc'))

try:
    from test_concentdice import TestConcentDice
finally:
    pass

if __name__ == "__main__":
    unittest.main()
