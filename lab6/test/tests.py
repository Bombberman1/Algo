import unittest
from ..src.trie import Trie, create_trie_with_words


class TrieTests(unittest.TestCase):
    words = [
        "film", "factory", "banana", "fabric", "board",
        "ban", "bones", "figure", "apple", "his", "him",
        "history", "actor", "apply", "open", "orion",
        "fit", "apollo", "fascinating", "opera", "bird",
        "horse", "house", "bingo", "archer", "hi"
    ]

    def test_add_word(self):
        trie = Trie()
        trie.add_word("change")
        expected = "c"
        [actual] = trie.root.children.keys()
        self.assertEqual(expected, actual)

    def test_add_word_empty(self):
        trie = Trie()
        trie.add_word("")
        expected = {}
        actual = trie.root.children
        self.assertEqual(expected, actual)

    def test_add_word_upper1(self):
        trie = Trie()
        trie.add_word("Bad")
        expected = {}
        actual = trie.root.children
        self.assertEqual(expected, actual)

    def test_add_word_upper2(self):
        trie = Trie()
        trie.add_word("bAd")
        expected = {}
        actual = trie.root.children
        self.assertEqual(expected, actual)

    def test_add_word_upper3(self):
        trie = Trie()
        trie.add_word("baD")
        expected = {}
        actual = trie.root.children
        self.assertEqual(expected, actual)

    def test_create_trie(self):
        expected_trie = Trie()
        expected_trie.add_word("young")
        expected_trie.add_word("old")
        expected_trie.add_word("offer")
        actual_trie = create_trie_with_words(["young", "old", "offer"])
        self.assertEqual(expected_trie.root.children.keys(), actual_trie.root.children.keys())

    def test_find_word1(self):
        trie = create_trie_with_words(self.words)
        actual = trie.find_word("figure")
        self.assertTrue(actual)

    def test_find_word2(self):
        trie = create_trie_with_words(self.words)
        actual = trie.find_word("fi")
        self.assertFalse(actual)

    def test_find_word3(self):
        trie = create_trie_with_words(self.words)
        actual = trie.find_word("hi")
        self.assertTrue(actual)

    def test_find_words_with_prefix1(self):
        trie = create_trie_with_words(self.words)
        expected = {"factory", "fabric", "fascinating"}
        actual = trie.find_words_with_prefix("fa")
        self.assertEqual(expected, set(actual))

    def test_find_words_with_prefix2(self):
        trie = create_trie_with_words(self.words)
        expected = {"apple", "actor", "apply", "apollo", "archer"}
        actual = trie.find_words_with_prefix("a")
        self.assertEqual(expected, set(actual))

    def test_find_words_with_prefix3(self):
        trie = create_trie_with_words(self.words)
        expected = {"his", "him", "history", "hi"}
        actual = trie.find_words_with_prefix("hi")
        self.assertEqual(expected, set(actual))

    def test_find_words_with_prefix4(self):
        trie = create_trie_with_words(self.words)
        expected = set(self.words)
        actual = trie.find_words_with_prefix("")
        self.assertEqual(expected, set(actual))


if __name__ == "__main__":
    unittest.main()
