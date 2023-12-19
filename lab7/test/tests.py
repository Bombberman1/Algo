import unittest

from lab7.src.file_func import input_from_file
from lab7.src.ling_game import play_ling_game, wchain_better


class LingTests(unittest.TestCase):
    def test_1_case(self):
        play_ling_game("wchainTest1.in.txt")
        file = open("wchain.out.txt")
        line_length = 0
        result = -2
        for line in file:
            line_length += 1
            if line_length == 1:
                result = int(line)
                file.close()
                break
        self.assertEqual(6, result)

    def test_2_case(self):
        play_ling_game("wchainTest2.in.txt")
        file = open("wchain.out.txt")
        line_length = 0
        result = -2
        for line in file:
            line_length += 1
            if line_length == 1:
                result = int(line)
                file.close()
                break
        self.assertEqual(4, result)

    def test_3_case(self):
        play_ling_game("wchainTest3.in.txt")
        file = open("wchain.out.txt")
        line_length = 0
        result = -2
        for line in file:
            line_length += 1
            if line_length == 1:
                result = int(line)
                file.close()
                break
        self.assertEqual(1, result)

    def test_4_case(self):
        play_ling_game("wchainTest4.in.txt")
        file = open("wchain.out.txt")
        line_length = 0
        result = -2
        for line in file:
            line_length += 1
            if line_length == 1:
                result = int(line)
                file.close()
                break
        self.assertEqual(6, result)

    def test_bad(self):
        play_ling_game("wchainTestBad.in.txt")
        file = open("wchain.out.txt")
        line_length = 0
        result = -2
        for line in file:
            line_length += 1
            if line_length == 1:
                result = int(line)
                file.close()
                break
        self.assertEqual(-1, result)

    def test_10000(self):
        play_ling_game("wchainTest10K.in.txt")
        file = open("wchain.out.txt")
        line_length = 0
        result = -2
        for line in file:
            line_length += 1
            if line_length == 1:
                result = int(line)
                file.close()
                break
        self.assertEqual(7, result)

    def test_1_faster(self):
        words = input_from_file("wchainTest1.in.txt")
        result = wchain_better(words)
        self.assertEqual(6, result)

    def test_2_faster(self):
        words = input_from_file("wchainTest2.in.txt")
        result = wchain_better(words)
        self.assertEqual(4, result)

    def test_3_faster(self):
        words = input_from_file("wchainTest3.in.txt")
        result = wchain_better(words)
        self.assertEqual(1, result)

    def test_4_faster(self):
        words = input_from_file("wchainTest4.in.txt")
        result = wchain_better(words)
        self.assertEqual(6, result)

    def test_bad_faster(self):
        words = input_from_file("wchainTestBad.in.txt")
        result = wchain_better(words)
        self.assertEqual(-1, result)

    def test_10K_faster(self):
        words = input_from_file("wchainTest10K.in.txt")
        result = wchain_better(words)
        self.assertEqual(7, result)


if __name__ == "__main__":
    unittest.main()
