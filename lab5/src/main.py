from find_road import find_bad_road

if __name__ == "__main__":
    gas_list = ["Gas1", "Gas2"]
    towns_list = ["Lviv", "Stryi", "Kyiv", "Sambir", "Dolyna", "Volyn", "Chernihiv"]
    available_connections = [
        ["Sambir", "Dolyna"],
        ["Lviv", "Stryi"],
        ["Dolyna", "Gas1"],
        ["Gas1", "Lviv"],
        ["Stryi", "Kyiv"],
        ["Volyn", "Gas1"],
        ["Gas2", "Chernihiv"],
        ["Chernihiv", "Volyn"],
    ]
    for bad_access in find_bad_road(gas_list, towns_list, available_connections):
        print(bad_access)
