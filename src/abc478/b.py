import itertools

N, V = map(int, input().split())
W = list(map(int, input().split()))
ans = 0
for v in itertools.combinations([i for i in range(N)], 3):
    v1, v2, v3 = v
    if v1 + v2 + v3 + 3 <= V:
        ans = max(ans, W[v1] + W[v2] + W[v3])

print(ans)
