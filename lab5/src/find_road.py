def find_bad_road(gas_list, towns_list, towns_logic):
    graph = {}
    no_access_towns_list = []

    for gas in gas_list:
        if gas not in graph:
            graph[gas] = []
        if gas not in graph[gas]:
            graph[gas].append(gas)

    for town in towns_list:
        if town not in graph:
            graph[town] = []
        if town not in graph[town]:
            graph[town].append(town)

    for town in towns_logic:
        if town[1] not in graph[town[0]]:
            graph[town[0]].append(town[1])

    for gas in gas_list:
        towns_from_gas = []
        visited = set()
        queue = [gas]
        while queue:
            town = queue.pop(0)
            if town not in visited:
                visited.add(town)
                towns_from_gas.append(town)
                queue.extend(graph[town])
                if town in gas_list and town != gas:
                    break
        no_access_towns = [
            no_access_town
            for no_access_town in towns_list
            if no_access_town not in towns_from_gas
        ]
        if no_access_towns:
            no_access_towns_list.append([gas, no_access_towns])

    if no_access_towns_list:
        return no_access_towns_list
    else:
        return []
