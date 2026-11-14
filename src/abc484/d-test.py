import random
from collections import defaultdict

N = 5
A = [1, 1, 3, 1, 1]
# A = [random.randint(1, 3) for i in range(N)]

print(A)


def gutyoku(N, A):
    res = set()
    res.add("[" + ", ".join([str(b) for b in A]) + "]")
    for i in range(N):
        for j in range(i):
            B = A[:]
            B[j] = A[i]
            for k in range(j + 1, i + 1):
                B[k] = A[k - 1]
            res.add("[" + ", ".join([str(b) for b in B]) + "]")
    return res


d = defaultdict(int)

ans = 0
for i in range(N):
    if i > 0 and A[i] == A[i - 1]:
        continue
    ans += i - d[A[i]]
    d[A[i]] += 1

print(ans + 1)

res = gutyoku(N, A)

print(ans + 1, len(res))
print(res)
