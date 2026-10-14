def inv_between_perms(P1, P2):
    n = len(P1)
    pos = [0] * n
    for i, v in enumerate(P1):
        pos[v] = i
    a = [pos[v] for v in P2]
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                ans += 1
    return ans


N, L = map(int, input().split())

dp = [-float("inf") for _ in range(N + 1)]
dp[0] = 0
C = [0]
P = [[i for i in range(L)]]

for i in range(N):
    data = list(map(int, input().split()))
    C.append(data[0])
    P.append([p - 1 for p in data[1:]])

for i in range(N + 1):
    for j in range(max(0, i - L * L), i):
        if inv_between_perms(P[j], P[i]) <= i - j:
            dp[i] = max(dp[i], dp[j] + C[i])

print(max(dp))
