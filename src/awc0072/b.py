N, K = map(int, input().split())
A = list(map(int, input().split()))

plus_rui = [0 for i in range(N + 1)]
minus_rui = [0 for i in range(N + 1)]
for i in range(N):
    plus_rui[i + 1] += plus_rui[i] + (A[i] if A[i] >= 0 else 0)
    minus_rui[i + 1] += minus_rui[i] + (A[i] if A[i] < 0 else 0)


ans = -float("inf")

for l in range(N - K + 1):
    ans = max(ans, plus_rui[N] + (minus_rui[l + K] - minus_rui[l]))

print(ans)
