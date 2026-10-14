N, M = map(int, input().split())
A = list(map(int, input().split()))
rA = [0 for i in range(N + 1)]
for i in range(N):
    rA[i + 1] += rA[i] + A[i]

ma = -float("inf")
mi = float("inf")

for i in range(M):
    L, R = map(int, input().split())
    ma = max(ma, rA[R] - rA[L - 1])
    mi = min(mi, rA[R] - rA[L - 1])

print(ma - mi)
