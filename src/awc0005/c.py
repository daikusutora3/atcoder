N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N - 1):
    if A[i] > A[i + 1] and A[i] - A[i + 1] > K:
        ans += (A[i] - K) - A[i + 1]
        A[i + 1] = A[i] - K

for i in range(N - 1, 0, -1):
    if A[i] > A[i - 1] and A[i] - A[i - 1] > K:
        ans += (A[i] - K) - A[i - 1]
        A[i - 1] = A[i] - K

print(ans)
