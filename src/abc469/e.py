N, K = map(int, input().split())
S = input()

cnt = 0
r = 0
# lに対して取る区間のoの数がK以上になるrの最小値
l_rmin = [-1 for i in range(N)]
for l in range(N):
    while r < N and cnt < K:
        cnt += 1 if S[r] == "o" else 0
        r += 1
    if cnt >= K:
        l_rmin[l] = r - 1
    cnt -= 1 if S[l] == "o" else 0


def is_ok(k):
    global N, K, S, l_rmin
    # print(l_rmin)
    rui = [0 for i in range(N + 1)]
    rui_max = [-float("inf") for i in range(N + 1)]
    for i in range(N):
        rui[i + 1] += rui[i] + (1 if S[i] == "o" else 0) - k
    rui_max = rui[:]
    for i in range(N - 1, -1, -1):
        rui_max[i] = max(rui_max[i + 1], rui[i])

    # print(rui_max)
    flag = False
    for l in range(N):
        rmin = l_rmin[l]
        if rmin == -1:
            break
        if rui_max[rmin] - rui[l] >= 0:
            flag = True
    return flag


ok = 0
ng = 1
eps = 10 ** (-6)
while abs(ng - ok) > eps:
    mid = (ok + ng) / 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
