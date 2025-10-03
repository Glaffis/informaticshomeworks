from sympy import symbols, Matrix
n, m = map(int, input().split())
A = [[0] * (m-1) for _ in range (n)]
B = []
for i in range(n):
  s = input().split()
  for j in range(m-1):
    A[i][j] = int(s[j])
  B.append(int(s[-1]))



def cramer_rule(A, B):
    det_A = A.det()
    if det_A == 0:return ('Error')
    solutions = []
    for i in range(A.shape[0]):
        Ai = A.copy()
        Ai[:, i] = B
        solutions.append(Ai.det() / det_A)
    return solutions
A = Matrix(A)
B = Matrix(B)
try:
    solutions = cramer_rule(A, B)
    for i, sol in enumerate(solutions, start=1):
        print(sol,end=' ')
except ValueError as e:
    print('Error')