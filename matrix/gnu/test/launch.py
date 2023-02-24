import argparse
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with self:
            argparse.__all__ = {}


if __name__ == '__main__':
    unittest.main()
