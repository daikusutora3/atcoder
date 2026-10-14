N, L, R = map(int, input().split())

T = list(map(int, input().split()))


rui = [0 for i in range(N + 1)]

for i in range(N):
    rui[i + 1] += rui[i] + (1 if L <= T[i] <= R else -1)

rui_max = [r for r in rui]
for i in range(N - 1, -1, -1):
    rui_max[i] = max(rui_max[i], rui_max[i + 1])

ans = -float("inf")
for l in range(N):
    ans = max(ans, rui_max[l + 1] - rui[l])

print(ans)
