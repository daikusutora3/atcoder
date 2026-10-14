N, K, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = N - K
cnt = 0
print(A[:K])
for i in range(K - 1, -1, -1):
    cnt += A[i]
    ans += 1
    if cnt >= X:
        break

print(ans if cnt >= X else -1)
