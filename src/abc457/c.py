N, K = map(int, input().split())
A = [list(map(int, input().split()))[1:] for i in range(N)]
C = list(map(int, input().split()))

ans = -1
for i in range(N):
    K -= len(A[i]) * C[i]
    if K <= 0:
        ans = A[i][(K - 1) % len(A[i])]
        break

print(ans)
