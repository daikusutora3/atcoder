from bisect import bisect_left, bisect_right


N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
AT = []
# これで転置できるよ
# list(map(list, list(zip(*A[::-1]))))
for i in range(M):
    row = []
    for vec in A:
        row.append(vec[i])
    AT.append(row)

for i in range(M):
    AT[i].sort()

R_AT = [[0 for j in range(N + 1)] for i in range(M)]
for i in range(M):
    for j in range(N):
        R_AT[i][j + 1] += R_AT[i][j] + AT[i][j]

ans = 0
for i in range(M):
    for j in range(N):
        bl = bisect_left(AT[i], AT[i][j])
        br = bisect_right(AT[i], AT[i][j])
        left = AT[i][j] * bl - R_AT[i][bl]
        right = (R_AT[i][N] - R_AT[i][br]) - AT[i][j] * (N - br)
        ans += left + right
        # print(AT[i])
        # print(f"{left} {AT[i][j]} {right}")

print(ans // 2)
