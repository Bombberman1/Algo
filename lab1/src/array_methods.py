def square_array(array: list) -> list:
    # array = [number ** 2 for number in array]

    # for start in range(len(array)):
    #     min_number_id = start
    #     for number_id in range(start + 1, len(array)):
    #         if array[min_number_id] > array[number_id]:
    #             min_number_id = number_id
    #     array[start], array[min_number_id] = array[min_number_id], array[start]
    # return array

    split = 0
    while split < len(array) and array[split] < 0:
        split += 1

    negative_id = split - 1
    positive_id = split
    result = []

    while negative_id >= 0 and positive_id < len(array):
        if abs(array[negative_id]) < abs(array[positive_id]):
            result.append(array[negative_id] ** 2)
            negative_id -= 1
        else:
            result.append(array[positive_id] ** 2)
            positive_id += 1

    while negative_id >= 0:
        result.append(array[negative_id] ** 2)
        negative_id -= 1

    while positive_id < len(array):
        result.append(array[positive_id] ** 2)
        positive_id += 1

    return result
