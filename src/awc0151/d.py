M, D = map(int, input().split())

LRV = [list(map(int, input().split())) for i in range(M)]

ans = 0
for l, _, _ in LRV:
    l = max(-l, 0)
    if l > D:
        continue
    r = max(0, min((D - l) // 2, l))
    if l < D - 2 * l:
        r = max(r, D - 2 * l)
    res = 0
    for L, R, V in LRV:
        if -l <= L <= r and -l <= R <= r:
            res += V
    ans = max(ans, res)

print(ans)
