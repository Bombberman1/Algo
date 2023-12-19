from lab7.src.file_func import input_from_file, output_in_file


def play_ling_game(url="wchain.in.txt") -> None:
    max_words_length = {}

    words = input_from_file(url)

    if words is None:
        output_in_file(-1)
        return

    for word in sorted(words, key=len):
        max_words_length[word] = 1

        # if len(word) - 1 not in [len(length) for length in max_words_length.keys()]:
        #     continue

        for index in range(len(word)):
            new_word = word[:index:] + word[index + 1::]

            if new_word in max_words_length:
                max_words_length[word] = max(max_words_length[word], max_words_length[new_word] + 1)

    output_in_file(max(max_words_length.values()))


def wchain_better(words):
    if words is None:
        return -1

    word_set = set(words)
    max_chain_length = 1
    memo = {}

    def find_deleted(word):
        nonlocal max_chain_length
        if word not in memo:
            memo[word] = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]
                if new_word in word_set:
                    memo[word] = max(memo[word], 1 + find_deleted(new_word))

            max_chain_length = max(max_chain_length, memo[word])

        return memo[word]

    for word in words:
        find_deleted(word)

    return max_chain_length
