import heapq
from collections import defaultdict

class johnson:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list) 
    
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
    
    def bellman(self, start):
        dist = [float('inf')] * (self.n + 1) 
        dist[start] = 0

        for _ in range(self.n):
            updated = False
            for u in range(self.n + 1):
                if dist[u] == float('inf'):
                    continue
                for v, w in self.graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        updated = True
            if not updated:
                break
        for u in range(self.n + 1):
            if dist[u] == float('inf'):
                continue
            for v, w in self.graph[u]:
                if dist[u] + w < dist[v]:
                    return None 
        return dist
    
    def dijkstra(self, start, h):
        dist = [float('inf')] * self.n
        dist[start] = 0
        pq = [(0, start)] 
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
            
            for v, w in self.graph[u]:
                w_new = w + h[u] - h[v]
                
                if dist[u] + w_new < dist[v]:
                    dist[v] = dist[u] + w_new
                    heapq.heappush(pq, (dist[v], v))
    
        for v in range(self.n):
            if dist[v] != float('inf'):
                dist[v] = dist[v] - h[start] + h[v]
        
        return dist
    
    def find_paths(self):

        for i in range(self.n):
            self.graph[self.n].append((i, 0))
        h = self.bellman(self.n)
        
        if h is None:
            return None
        distances = []
        for i in range(self.n):
            dist = self.dijkstra(i, h)
            distances.append(dist)
        
        return distances