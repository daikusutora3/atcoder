from bisect import bisect_left

N, K, X = map(int, input().split())
A = list(map(int, input().split()))

rui = [0 for i in range(N + 1)]

for i in range(N):
    rui[i + 1] += rui[i] + A[i]

ans = 0

# 4 3 6
# 3 1 4 2

for i in range(N):
    bl = bisect_left(rui, X + rui[i])
    ans += max(0, min(i + K + 1, N + 1) - (bl))
    # print(f"[{i}, {min(i + K + 1, N + 1)}), [{bl}, {N + 1})")
    # print(max(0, min(i + K + 1, N + 1) - (bl)))

print(ans)
