N, D = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i in range(N - 1):
    if abs(A[i] - A[i + 1]) > D:
        ans += abs(A[i] - A[i + 1])

print(ans)
