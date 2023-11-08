from short_path import short_path
from graph_input import create_matrix_from_graph
from path_output import output_short_way

if __name__ == "__main__":
    matrix = create_matrix_from_graph("input.txt")
    shortest_path = short_path(matrix)
    output_short_way("output.txt", shortest_path)
