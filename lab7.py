import csv
from collections import deque

def bfs(capacity, source, sink, parent):
    visited = {source}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v, cap in capacity.get(u, {}).items():
            if v not in visited and cap > 0:
                parent[v] = u
                visited.add(v)
                if v == sink:
                    return True
                queue.append(v)
    return False

def max_flow(farms, shops, roads):
    source, sink = "SUPER_SOURCE", "SUPER_SINK"
    capacity = {}

    def add_edge(u, v, cap):
        if u not in capacity: capacity[u] = {}
        if v not in capacity: capacity[v] = {}
        capacity[u][v] = capacity[u].get(v, 0) + cap
        if u not in capacity[v]: capacity[v][u] = 0

    for f in farms: add_edge(source, f, float("inf"))
    for s in shops: add_edge(s, sink, float("inf"))
    for u, v, cap in roads: add_edge(u, v, cap)

    max_f = 0
    parent = {}
    while bfs(capacity, source, sink, parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        max_f += path_flow
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
        parent = {}
    return max_f

def load_data(file_path):
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        farms = [x.strip() for x in next(reader)]
        shops = [x.strip() for x in next(reader)]
        roads = [(r[0].strip(), r[1].strip(), int(r[2].strip())) for r in reader if r]
    return farms, shops, roads

if __name__ == "__main__":
    try:
        f_list, s_list, r_list = load_data("roads.csv")
        print(f"Результат: {max_flow(f_list, s_list, r_list)}")
    except FileNotFoundError:
        print("Помилка: Файл roads.csv не знайдено.")


