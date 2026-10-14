N, P = map(int, input().split())


def is_ok(k, a, b):
    global P
    return a * k + b <= P


res = []

for _ in range(N):
    H, G = map(int, input().split())
    ok = -1
    ng = 10**10
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, G, H):
            ok = mid
        else:
            ng = mid
    res.append(ok)

res.sort()


ans = True
for i in range(N):
    if res[i] == -1 or not (res[i] >= i):
        ans = False


print("Yes" if ans else "No")
