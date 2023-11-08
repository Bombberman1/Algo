import re


def create_matrix_from_graph(name):
    graph_file = open(name)
    matrix = []
    for line in graph_file:
        if re.search("\\d", line):
            digit_line = re.findall("\\d", line)
            matrix_row = []
            for digit in digit_line:
                matrix_row.append(int(digit))
            matrix.append(matrix_row)

    return matrix
