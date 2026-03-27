from collections import deque

def credits_conditions(entprs_demand, banks_supply):

    n_entprs = len(entprs_demand)
    n_banks = len(banks_supply)
    total_demand = sum(entprs_demand)
    total_supply = sum(banks_supply)
    if total_supply < total_demand:
        return False
    
    S = 0
    T = n_banks+n_entprs+1
    total_vertices = sink+1
    capacity=[[0] * total_vertices for _ in range(total_vertices)]
    graph=[[] for _ in range(total_vertices)]
    for j in range(n_banks):
        bank_node = j+1
        capacity[source][bank_node] = banks_supply[j]
        graph[source].append(bank_node)
        graph[bank_node].append(source)
    for i in range(n_entprs):
        entprs_node = n_banks+i+1
        capacity[entprs_node][T] = entprs_demand[i]
        graph[entprs_node].append(T)
        graph[T].append(entprs_node)
    INF = total_demand + 1
    for j in range(n_banks):
        bank_node = j + 1
        for i in range(n_entprs):
            entprs_node=n_banks + i + 1
            capacity[bank_node][entprs_node] = INF
            graph[bank_node].append(entprs_node)
            graph[entprs_node].append(bank_node)
    max_flow = 0
    while True:
        parent = [-1] * total_vertices
        parent[S] = S
        queue = deque([S])
        while queue:
            u = queue.popleft()
            if u == T:
                break
            for v in graph[u]:
                if parent[v] == -1 and capacity[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
        if parent[T] == -1:
            break
        path_flow = float('inf')
        v = T
        while v != S:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u
        max_flow += path_flow
        v = T
        while v != S:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u
        return max_flow == total_demand
