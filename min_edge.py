def min_edge(n_left, n_right, edges):
    adj = [[] for _ in range(n_left + 1)]
    for u, v in edges:
        adj[u].append(v)
    match_right = [-1] * (n_right + 1)
    match_left = [-1] * (n_left + 1)
    def circuit_search(start_u):
        cur = [False] * (n_right + 1)
        stack = [(start_u, 0)]
        path = {}
        
        while stack:
            u, idx = stack[-1]
            if idx >= len(adj[u]):
                stack.pop()
                continue
            v = adj[u][idx]
            stack[-1] = (u, idx + 1)
            if used[v]:
                continue
            cur[v] = True
            path[v] = u
            if match_right[v] == -1:
                curr_v = v
                while curr_v != -1 and curr_v in path:
                    curr_u = path[curr_v]
                    prev_v = match_left[curr_u]
                    match_right[curr_v] = curr_u
                    match_left[curr_u] = curr_v
                    curr_v = prev_v
                return True
            else:
                u_next = match_right[v]
                stack.append((next_u, 0))
        return False
    matching_size = 0
    for u in range(1, n_left + 1):
        if circuit_search(u):
            matching_size += 1
    cover_size = (n_left + n_right) - matching_size
    cover = []
    for v in range(1, n_right + 1):
        if match_right[v] != -1:
            u = match_right[v]
            cover.append((u, v))
    for u in range(1, n_left + 1):
        if match_left[u] == -1:
            if adj[u]:
                cover.append((u, adj[u][0]))
    for v in range(1, n_right + 1):
        if match_right[v] == -1:
            for u in range(1, n_left + 1):
                if v in adj[u]:
                    cover.append((u, v))
                    break
    return cover