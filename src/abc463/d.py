N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(N)]
LR.sort(key=lambda x: x[1])


ok = -1
ng = 10**10


def is_ok(k):
    global N, K, LR
    br = -float("inf")
    cnt = 0
    for l, r in LR:
        if l - br >= max(k, 1):
            cnt += 1
            br = r
    return cnt >= K


while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
