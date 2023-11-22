import unittest

from lab1.src.array_methods import square_array


class ArrayMethodTests(unittest.TestCase):
    def test_with_negative(self):
        array = [-18, -2, 0, 3, 5, 10, 30, 40]
        expected = [0, 4, 9, 25, 100, 324, 900, 1600]
        actual = square_array(array)
        self.assertEqual(expected, actual)

    def test_all_negative(self):
        array = [-10, -7, -5, -2]
        expected = [4, 25, 49, 100]
        actual = square_array(array)
        self.assertEqual(expected, actual)

    def test_all_positive(self):
        array = [2, 4, 5, 7, 8, 10]
        expected = [4, 16, 25, 49, 64, 100]
        actual = square_array(array)
        self.assertEqual(expected, actual)

    def test_task1(self):
        array = [-4, -2, 0, 1, 3]
        expected = [0, 1, 4, 9, 16]
        actual = square_array(array)
        self.assertEqual(expected, actual)

    def test_task2(self):
        array = [1, 2, 3, 4, 5]
        expected = [1, 4, 9, 16, 25]
        actual = square_array(array)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
