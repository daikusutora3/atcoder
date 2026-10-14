N, M = map(int, input().split())

ans = [0 for i in range(M)]

P = list(map(int, input().split()))

for i in range(N):
    p = P[i] - 1
    while p < M and ans[p] != 0:
        p += 1
    if p < M:
        ans[p] = 1

print(sum(ans))
