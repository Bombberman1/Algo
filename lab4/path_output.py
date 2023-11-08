def output_short_way(path, shortest_path):
    output_file = open(path, "w")
    output_file.write(f"Length: {shortest_path}\nPath: {shortest_path}" if type(shortest_path) is int else
                      f"Length: {len(shortest_path)}\nPath: {shortest_path}")
    output_file.close()
