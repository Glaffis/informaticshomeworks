skyscr = list(map(int,input().split()))
a = len(skyscr)
res = []
for i in range(a):
    current_skyscr = skyscr[i]
    if i == 0:
        res.append(-1)
        continue
    found = False
    for j in range(i-1,-1,-1):
        if skyscr[j]>=current_skyscr:
            res.append(j)
            found = True
            break
    if not found:
            res.append(-1)
print(*res)