from itertools import permutations

from more_itertools import distinct_permutations

N = int(input())
A = list(map(int, input().split()))
OP = list(input().split())
ansma = 0
ansmi = float("inf")
for pA in permutations(A, N):
    for pOP in distinct_permutations(OP, N):
        now = 0
        for i in range(N):
            if pOP[i] == "^":
                now ^= pA[i]
            else:
                now += pA[i]
        ansma = max(ansma, now)
        ansmi = min(ansmi, now)


print(ansma, ansmi)
