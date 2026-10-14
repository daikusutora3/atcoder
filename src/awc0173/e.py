import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))
rui = [0 for i in range(N + 1)]

if K == 0:
    print(sum(A))
    sys.exit()
elif K >= N:
    K = N - 1

for i in range(N):
    rui[i + 1] += rui[i] + A[i]

best = [[[0 for r in range(N)] for l in range(N)] for i in range(N)]

for i in range(K):
    best[i][0][0] = (rui[i + N - K + 1] - rui[i]) * 2

for i in range(N):
    for l in range(i + 1):
        for r in range(N - i - (N - K + 1) + 1):
            if l == r == 0:
                continue
            if l > 0:
                best[i][l][r] = max(best[i][l][r], (best[i][l - 1][r] + A[i - l]) * 2)
            if r > 0:
                best[i][l][r] = max(
                    best[i][l][r], (best[i][l][r - 1] + A[i + N - K + r]) * 2
                )

ans = 0
for be in best:
    for b in be:
        ans = max(ans, max(b))
print(ans)
