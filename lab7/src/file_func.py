import re


def input_from_file(url: str):
    file = open(url)
    words = []
    line_length = 0
    array_length = 0
    for line in file:
        line_length += 1
        if line_length == 1:
            array_length = int(line)
        for word in re.findall("[A-z]+", line):
            if not re.search("[A-Z]", word):
                words.append(word)

    file.close()

    if 1 <= array_length <= 10 ** 5 and array_length == len(words):
        return words


def output_in_file(length: int):
    file = open("wchain.out.txt", "w")
    file.write(str(length) + "\n")
    file.close()
