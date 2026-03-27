from collections import deque

def Edmond_Karp(n, graph, capacity, S, T):
    max_flow = 0
    while True:
        parent = [-1] * (n+1)
        parent[S] = S
        queue = deque([S])
        path_found = False
        while queue:
            u = queue.popleft()
            if u == T:
                path_found = True
                break
            for v in graph[u]:
                if parent[v] == -1 and capacity[u][v] > 0:
                    parent[v] = u
                    queue.append(v)   
        
        if not path_found:
            break
        path_flow = float('inf')
        v=T
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
        return max_flow