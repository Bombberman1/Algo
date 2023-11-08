def short_path(matrix_list):
    bombs = []
    for bomb_row in range(len(matrix_list)):
        for bomb_cell in range(len(matrix_list[0])):
            if matrix_list[bomb_row][bomb_cell] == 0:
                bombs.append((bomb_row, bomb_cell))

    for bomb in bombs:
        bomb_row, bomb_cell = bomb
        for bomb_row_available in range(bomb_row - 1, bomb_row + 2):
            for bomb_cell_available in range(bomb_cell - 1, bomb_cell + 2):
                if bomb_row_available != -1 \
                        and bomb_row_available != len(matrix_list) \
                        and bomb_cell_available != -1 \
                        and bomb_cell_available != len(matrix_list[0]):
                    matrix_list[bomb_row_available][bomb_cell_available] = 0

    def is_normal_index(selected_row, selected_cell):
        return 0 <= selected_row < len(matrix_list) \
            and 0 <= selected_cell < len(matrix_list[0]) \
            and matrix_list[selected_row][selected_cell] == 1

    def neighbors(selected_row, selected_cell):
        return [
            (selected_row - 1, selected_cell), (selected_row, selected_cell - 1),
            (selected_row + 1, selected_cell), (selected_row, selected_cell + 1)
        ]

    available = [(row, 0) for row in range(len(matrix_list)) if matrix_list[row][0] == 1]
    visited = set(available)
    path = {}

    while available:
        row, cell = available.pop(0)

        if cell == len(matrix_list[0]) - 1:
            shortest_path = [(row, cell)]
            while (row, cell) in path:
                row, cell = path[(row, cell)]
                shortest_path.insert(0, (row, cell))
            return shortest_path

        for neighbor_row, neighbor_cell in neighbors(row, cell):
            if is_normal_index(neighbor_row, neighbor_cell) and (neighbor_row, neighbor_cell) not in visited:
                available.append((neighbor_row, neighbor_cell))
                visited.add((neighbor_row, neighbor_cell))
                path[(neighbor_row, neighbor_cell)] = (row, cell)

    return -1
