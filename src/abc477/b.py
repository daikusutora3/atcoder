N, D = map(int, input().split())

X = list(map(int, input().split()))

X = [(X[i], i) for i in range(N)]
X.sort()

ans = []
for i in range(N):
    flag = True
    if i > 0 and abs(X[i - 1][0] - X[i][0]) < D:
        flag = False
    if i < N - 1 and abs(X[i + 1][0] - X[i][0]) < D:
        flag = False
    if flag:
        ans.append(X[i][1] + 1)

ans.sort()
print(len(ans))
print(*ans)
