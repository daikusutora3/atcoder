N, T = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
time = 0
for i in range(N):
    ans += max(0, A[i] - time)
    if A[i] - time >= 0:
        time = A[i] + 100

ans += max(0, T - time)
print(ans)
