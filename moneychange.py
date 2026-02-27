n, m = map(int, input().split())

edges = []
for _ in range(m):
    v1, v2, rate = input().split()
    edges.append((int(v1)-1, int(v2)-1, float(rate)))

money = [0.0] * n
money[0] = 1.0

for _ in range(n - 1):
    for u, v, r in edges:
        if money[u] * r > money[v]:
            money[v] = money[u] * r

for u, v, r in edges:
    if money[u] * r > money[v]:
        print("YES")
        exit()

print("NO")