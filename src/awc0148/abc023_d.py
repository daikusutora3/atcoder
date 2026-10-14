N = int(input())
HS = [list(map(int, input().split())) for i in range(N)]
time = [-1 for i in range(N)]


def is_ok(k):
    global N, HS, time
    for i in range(N):
        b, a = HS[i]
        t = max(-1, (k - b) // a)
        time[i] = t
    time.sort()
    res = True
    for i in range(N):
        if time[i] == -1 or not (time[i] >= i):
            res = False
    return res


ok = 10**15
ng = 0

while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
