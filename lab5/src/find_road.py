from .file_func import out_result


def bfs(graph_elem, gas_list_elem, gas_elem, towns_from_gas_elem):
    visited = set()
    queue = [gas_elem]
    while queue:
        town = queue.pop(0)
        if town not in visited:
            visited.add(town)
            towns_from_gas_elem.append(town)
            queue.extend(graph_elem[town])
            if town in gas_list_elem and town != gas_elem:
                break


def find_bad_road(gas_list, towns_list, towns_logic, out_file=False):
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
        bfs(graph, gas_list, gas, towns_from_gas)

        no_access_towns = [
            no_access_town
            for no_access_town in towns_list
            if no_access_town not in towns_from_gas
        ]
        if no_access_towns:
            no_access_towns_list.append([gas, no_access_towns])

    if no_access_towns_list:
        if out_file:
            out_result(no_access_towns_list)
        return no_access_towns_list
    else:
        return []
