import unittest

import calc


class TestSample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.sum(10, 20), 30)

    def test_boolean(self):
        self.assertTrue(calc.sum(10, 20) == 30)


if __name__ == '__main__':
    unittest.main()
