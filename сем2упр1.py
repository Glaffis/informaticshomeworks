l = list(map(int, input().split()))
n = l[0]
all = n * (n + 1) // 2
s = sum(l) - n
print(all - s)