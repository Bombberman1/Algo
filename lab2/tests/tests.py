import unittest

from lab2.src.pocker_game import play_pocker


class PockerTests(unittest.TestCase):
    def test_1(self):
        array = [9, 0, 10, 13, 8, 4, 0, 1]
        actual = play_pocker(array)
        self.assertEqual(6, actual)

    def test_2(self):
        array = [0, 10, 15, 50, 0, 14, 9, 12, 40]
        actual = play_pocker(array)
        self.assertEqual(7, actual)

    def test_3(self):
        array = [1, 1, 1, 2, 1, 1, 3]
        actual = play_pocker(array)
        self.assertEqual(3, actual)

    def test_4(self):
        array = [5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5, 0, 0]
        actual = play_pocker(array)
        self.assertEqual(4, actual)

    def test_5(self):
        array = [0, 6, 9, 11, 12, 13, 0]
        actual = play_pocker(array)
        self.assertEqual(6, actual)


if __name__ == "__main__":
    unittest.main()
