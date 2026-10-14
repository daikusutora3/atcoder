N, M = map(int, input().split())

R = list(map(int, input().split()))

ans = 0
for _ in range(M):
    f, s = map(int, input().split())
    if R[f - 1] >= s:
        R[f - 1] -= s
        ans += 1

print(ans)
