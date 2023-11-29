from lab6.src.file_func import output_prefix_words


class Node:
    def __init__(self):
        self.children = {}
        self.word_end = False


def check_is_uppercase(word: str) -> bool:
    for character in word:
        if character.isupper():
            return True

    return False


class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word: str):
        node = self.root
        if not check_is_uppercase(word):
            for character in word:
                if character not in node.children:
                    node.children[character] = Node()
                node = node.children[character]
            node.word_end = True

    def find_word(self, word: str) -> bool:
        node = self.root
        for character in word:
            if character not in node.children:
                return False
            node = node.children[character]

        return node.word_end

    def find_word_with_propositions(self, word: str) -> list:
        node = self.root
        start_node_prefix = ""
        for character in word:
            if character not in node.children:
                return [False, []]
            start_node_prefix += character
            node = node.children[character]
        node_is_end = node.word_end

        if not node_is_end:
            proposition_words = []
            stack = [(node, start_node_prefix)]
            while stack:
                node, general_prefix = stack.pop()
                for character, value in node.children.items():
                    current_prefix = general_prefix + character
                    if value.word_end:
                        proposition_words.append(current_prefix)
                    stack.append((value, current_prefix))

            return [node_is_end, proposition_words]

        return [node_is_end]

    def find_words_with_prefix(self, find_prefix: str, output_in_file=False) -> list:
        words = []

        start_node_prefix = ""
        start_node = self.root
        for character in find_prefix:
            if character not in start_node.children:
                return []
            start_node_prefix += character
            start_node = start_node.children[character]

        if start_node.word_end:
            words.append(find_prefix)

        stack = [(start_node, start_node_prefix)]
        while stack:
            node, general_prefix = stack.pop()
            for character, value in node.children.items():
                current_prefix = general_prefix + character
                if value.word_end:
                    words.append(current_prefix)
                stack.append((value, current_prefix))

        if output_in_file:
            output_prefix_words(words)

        return words


def create_trie_with_words(words: list) -> Trie:
    trie = Trie()
    for word in words:
        trie.add_word(word)

    return trie
