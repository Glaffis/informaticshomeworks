def if_euler_in(graph, N):
    c = 0
    start = 0
    for i in range(N):
        if len(graph[i]) % 2 != 0:
            c += 1
            start = i
    if c not in [0, 2]:
        return None
        
    total_edges = sum(len(graph[i]) for i in range(N)) // 2
    if total_edges == 0:
        return [0] 

    has_edges = False
    for i in range(N):
        if len(graph[i]) > 0:
            has_edges = True
            start = i  
            break
    
    if not has_edges:
        return [0]
    
    g = {i: set(graph[i]) for i in range(N)}
    
    path = []
    
    def dfs_euler(v):
        while len(g[v]) > 0:
            u = g[v].pop()  
            g[u].remove(v)
            dfs_euler(u)    
        path.append(v)          
    
    dfs_euler(start)
    path.reverse() 
    
    if len(path) != total_edges + 1:
        return None  
    return path


