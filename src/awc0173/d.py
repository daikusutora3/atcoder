N, M = map(int, input().split())
H = list(map(int, input().split()))
damage = [0 for i in range(M + 1)]
for _ in range(N):
    L, R, A = map(int, input().split())
    damage[L - 1] -= A
    damage[R] += A

for i in range(M):
    damage[i + 1] += damage[i]

ans = 0
for i in range(M):
    if damage[i] + H[i] <= 0:
        ans += 1
print(ans)
