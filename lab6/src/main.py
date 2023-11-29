from lab6.src.file_func import get_words_from_file
from lab6.src.trie import create_trie_with_words

if __name__ == "__main__":
    trie = create_trie_with_words([
        "film", "factory", "banana", "fabric", "board",
        "ban", "bones", "figure", "apple", "his", "him",
        "history", "actor", "apply"
    ])
    print(trie.find_word("banana"))
    print(trie.find_word("his"))
    print(trie.find_word("fi"))
    print(trie.find_words_with_prefix("ap", output_in_file=True))
    print(trie.find_word_with_propositions("ba"))

    print(get_words_from_file())
