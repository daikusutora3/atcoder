N, M, D = map(int, input().split())

A = list(map(int, input().split()))

res = [i for i in range(N)]
LOGK = 61
doubling = [[0 for i in range(N)] for k in range(LOGK + 1)]

for a in A:
    res[a - 1], res[a] = res[a], res[a - 1]


for i in range(N):
    doubling[0][res[i]] = i

for k in range(LOGK):
    for i in range(N):
        doubling[k + 1][i] = doubling[k][doubling[k][i]]


for i in range(N):
    now = i
    for k in range(LOGK):
        if D >> k & 1:
            now = doubling[k][now]
    print(now + 1)
