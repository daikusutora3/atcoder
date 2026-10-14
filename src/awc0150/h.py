N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
rui = [0 for i in range(N + 1)]
for i in range(N):
    rui[i + 1] = rui[i] + A[i]

ans = 0

for a in range((K + 1) // 2, K // 2 + 2):
    b = K + 1 - a
    if a == b:
        res = (rui[N] - rui[N - b]) * 2 - A[N - b] - (rui[a] * 2 - A[a - 1])
        ans = max(ans, res)
    elif a == b + 1:
        res = (rui[N] - rui[N - b]) * 2 - (rui[a] * 2 - A[a - 1] - A[a - 2])
        ans = max(ans, res)
    elif a + 1 == b:
        res = (rui[N] - rui[N - b]) * 2 - A[N - b] - A[N - b + 1] - (rui[a] * 2)
        ans = max(ans, res)
print(ans)
