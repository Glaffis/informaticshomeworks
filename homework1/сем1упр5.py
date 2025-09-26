N = input()
b = int(input())
c = int(input())
N_10 = 0
for i in range(len(N)):
    N_10 += int(N[i]) * (b ** (len(N) - 1 - i))
if N_10 == 0:
    print("0")
else:
    res = []
    while N_10:
        res.append(str(N_10 % c))
        N_10 //= c
    print(''.join(res[::-1]))