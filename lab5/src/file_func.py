import re


def get_lists() -> list:
    file = open("input.txt")
    line_count = 1
    result = []
    gas_town_connection = []
    for line in file:
        regex_read = re.findall("\w+", line)
        if line_count < 3:
            result.append([elem for elem in regex_read])
        if line_count >= 3:
            gas_town_connection.append([elem for elem in regex_read])
        line_count += 1
    result.append(gas_town_connection)
    return result


def out_result(result: list):
    file = open("output.txt", "w")
    for gas_problem in result:
        file.write(str(gas_problem) + "\n")
