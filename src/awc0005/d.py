N, K = map(int, input().split())
A = list(map(int, input().split()))

ok, ng = 0, 10**15


def is_ok(k):
    global N, A, K
    num = 1
    s = 0
    for i in range(N):
        s += A[i]
        if s >= k and num < K:
            s = 0
            num += 1
    return num >= K and s >= k


while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
