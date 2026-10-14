N, Q = map(int, input().split())
LRX = [list(map(int, input().split())) for i in range(Q)]
LRX.sort(key=lambda x: (x[2], x[0], x[1]))

# 8 5
# 2 5 1
# 1 4 1
# 7 8 1
# 3 6 1
# 2 5 1

MAXR = [0 for i in range(Q + 1)]
imos = [0 for i in range(N + 1)]
for i in range(Q):
    L, R, X = LRX[i]
    if L <= MAXR[X]:
        imos[MAXR[X]] += 1
        MAXR[X] = max(R, MAXR[X])
        imos[MAXR[X]] -= 1
    else:
        MAXR[X] = max(MAXR[X], R)
        imos[L - 1] += 1
        imos[R] -= 1

for i in range(N):
    imos[i + 1] += imos[i]

print(*imos[:-1])
