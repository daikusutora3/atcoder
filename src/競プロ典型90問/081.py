N, K = map(int, input().split())

MAXK = 5000
rui = [[0 for j in range(MAXK + 1)] for i in range(MAXK + 1)]


for _ in range(N):
    a, b = map(int, input().split())
    rui[a][b] += 1


for i in range(1, MAXK + 1):
    for j in range(1, MAXK + 1):
        rui[i][j] += rui[i - 1][j] + rui[i][j - 1] - rui[i - 1][j - 1]


# for r in rui:
#     print(r)

ans = 0
for i in range(MAXK - K):
    for j in range(MAXK - K):
        ans = max(
            ans,
            rui[i + K + 1][j + K + 1]
            - rui[i][j + K + 1]
            - rui[i + K + 1][j]
            + rui[i][j],
        )

print(ans)
