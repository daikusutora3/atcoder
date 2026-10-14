from bisect import bisect_right


N, M, K = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

rui_A = [0 for i in range(N + 1)]
for i in range(N):
    rui_A[i + 1] += rui_A[i] + A[i]

ans = bisect_right(rui_A, X + Y * K) - 1
for j in range(M):
    if Y - (B[j] + K - 1) // K < 0:
        break
    Y -= (B[j] + K - 1) // K
    X += (-B[j]) % K
    money = X + Y * K
    bl = bisect_right(rui_A, money)
    ans = max(ans, j + bl)

print(ans)
