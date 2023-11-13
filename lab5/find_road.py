def find_bad_road(towns_logic):
    graph = {}
    bad_access_towns = []
    global_towns_roads = []
    smart_towns_roads = []

    for town in towns_logic:
        if town[0] not in graph:
            if town[0] not in graph:
                graph[town[0]] = []
        if town[1] not in graph:
            if town[1] not in graph:
                graph[town[1]] = []
        if town[1] not in graph[town[0]]:
            graph[town[0]].append(town[1])

    for town in towns_logic:
        towns_from_gas = []
        visited = set()
        queue = [town[0]]
        while queue:
            town = queue.pop(0)
            if town not in visited:
                visited.add(town)
                towns_from_gas.append(town)
                queue.extend(graph[town])
        global_towns_roads.append(towns_from_gas)

    for town1 in global_towns_roads:
        duplicate = False
        for town2 in global_towns_roads:
            if town1 != town2 and set(town1).issubset(set(town2)):
                duplicate = True
                break
        if not duplicate:
            smart_towns_roads.append(town1)

    for town in towns_logic:
        for smart_towns in smart_towns_roads:
            slicing_index = 0
            for smart_town_index in range(len(smart_towns)):
                if smart_towns[smart_town_index] == town[0]:
                    slicing_index = smart_town_index
            if slicing_index > 0:
                founded = False
                for bad_access_town in bad_access_towns:
                    if bad_access_town[0] == town[0]:
                        for item in smart_towns[:slicing_index:]:
                            bad_access_town[1].add(item)
                        founded = True
                        break
                if not founded:
                    bad_access_towns.append([town[0], set(smart_towns[:slicing_index:])])

    if len(bad_access_towns):
        return bad_access_towns
    else:
        return []
