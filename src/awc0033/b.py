N, K, L, R = map(int, input().split())
T = list(map(int, input().split()))

T_diff = []
for t in T:
    if L <= t <= R:
        T_diff.append(0)
    else:
        T_diff.append(min(abs(t - L), abs(t - R)))

T_diff.sort()

ans = 0
for i in range(K):
    ans += T_diff[i]

print(ans)
