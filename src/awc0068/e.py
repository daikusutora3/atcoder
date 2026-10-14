from sortedcontainers import SortedList


N, K = map(int, input().split())

A = [list(map(int, input().split())) for i in range(N)]

ruiA = [[0 for j in range(N + 1)] for i in range(N + 1)]

for i in range(N):
    for j in range(N):
        ruiA[i + 1][j + 1] = ruiA[i][j + 1] + ruiA[i + 1][j] - ruiA[i][j] + A[i][j]

n = N - K + 1
XA = [[-float("inf") for j in range(n)] for i in range(N)]
for i in range(N):
    s = SortedList(A[i][:K])
    XA[i][0] = s[-1]
    for j in range(n - 1):
        s.discard(A[i][j])
        s.add(A[i][j + K])
        XA[i][j + 1] = s[-1]

XYA = [[-float("inf") for j in range(n)] for i in range(n)]
for j in range(n):
    init_s = []
    for i in range(K):
        init_s.append(XA[i][j])
    s = SortedList(init_s)
    XYA[0][j] = s[-1]
    for i in range(n - 1):
        s.discard(XA[i][j])
        s.add(XA[i + K][j])
        XYA[i + 1][j] = s[-1]

ans = 0

for i in range(n):
    for j in range(n):
        ans = max(
            ans,
            ruiA[i + K][j + K]
            - ruiA[i][j + K]
            - ruiA[i + K][j]
            + ruiA[i][j]
            - XYA[i][j],
        )

print(ans)
