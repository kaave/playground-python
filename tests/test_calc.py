import unittest

from memo import calc


class TestSample(unittest.TestCase):
    def setUpClass():
        print('*** 全体前処理 ***')

    def tearDownClass():
        print('*** 全体後処理 ***')

    def setUp(self):
        print('+ テスト前処理')

    def tearDown(self):
        print('+ テスト後処理')

    def test_add(self):
        self.assertEqual(calc.add(10, 20), 30)

    def test_boolean(self):
        self.assertTrue(calc.add(10, 20) == 30)


if __name__ == '__main__':
    unittest.main()
