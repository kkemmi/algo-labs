def dfs(graph, start, visited):
    if start in visited:
        return
    visited.add(start)
    for neighbor in graph[start]:
        dfs(graph, neighbor, visited)

def find_unreachable_cities(storages, cities, pipelines):
    from collections import defaultdict
    graph = defaultdict(list)
    for src, dst in pipelines:
        graph[src].append(dst)

    result = []
    for storage in storages:
        visited = set()
        dfs(graph, storage, visited)
        unreachable = [city for city in cities if city not in visited]
        if unreachable:
            result.append([storage, unreachable])
    return result
