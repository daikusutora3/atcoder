N, M, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for _ in range(M):
    S, P, D = map(int, input().split())
    if S == 1:
        ans += max(0, A[P - 1] - K) * D
    else:
        ans += A[P - 1] * D

print(ans)
