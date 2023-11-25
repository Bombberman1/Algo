from lab5.src.find_road import find_bad_road
from lab5.src.file_func import get_lists

if __name__ == "__main__":
    # gas_list = ["Gas1", "Gas2"]
    # towns_list = ["Lviv", "Stryi", "Kyiv", "Sambir", "Dolyna", "Volyn", "Chernihiv"]
    # available_connections = [
    #     ["Sambir", "Dolyna"],
    #     ["Lviv", "Stryi"],
    #     ["Dolyna", "Gas1"],
    #     ["Gas1", "Lviv"],
    #     ["Stryi", "Kyiv"],
    #     ["Volyn", "Gas1"],
    #     ["Gas2", "Chernihiv"],
    #     ["Chernihiv", "Volyn"],
    # ]
    gas_list, towns_list, available_connections = get_lists()
    for bad_access in find_bad_road(gas_list, towns_list, available_connections, out_file=True):
        print(bad_access)
