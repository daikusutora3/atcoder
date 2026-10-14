from collections import defaultdict
import itertools


N, K, Q = map(int, input().split())
S = input()
C = list(input().split())
ABX = [list(input().split()) for i in range(N)]
d = defaultdict(int)

for perm in itertools.permutations(range(N)):
    lamp = list(S)
    res = []
    for i in perm:
        A, B, X = ABX[i]
        flag = True
        for j in range(K):
            if A[j] == "1" and lamp[j] != "1":
                flag = False
            if B[j] == "1" and lamp[j] != "0":
                flag = False

        if not flag:
            break
        for j in range(K):
            if X[j] == "1":
                lamp[j] = "0" if lamp[j] == "1" else "1"
        res.append(str(lamp.count("1")))
    if len(res) == N:
        d[",".join(res)] += 1

for _ in range(Q):
    T, Y = map(int, input().split())
    C[T - 1] = str(Y)
    print(d[",".join(C)])
