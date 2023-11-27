import re


def get_words_from_file() -> list:
    file = open("input.txt")
    words = []
    for line in file:
        for word in re.findall("[a-z]+", line):
            words.append(word)

    return words


def output_prefix_words(words: list):
    file = open("output.txt", "w")
    for word in words:
        file.write(word + "\n")
