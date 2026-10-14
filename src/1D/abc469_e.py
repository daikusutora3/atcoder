from collections import deque

N, K = map(int, input().split())

S = input()


def is_ok(k):
    # kパーセント以上が可能ですか？
    global N, K, S
    res = []
    for s in S:
        if s == "o":
            res.append(1 - k)
        else:
            res.append(-k)
    rui = [0 for i in range(N + 1)]
    for i in range(N):
        rui[i + 1] += rui[i] + res[i]
    rui_min = [0 for i in range(N + 1)]
    for i in range(N):
        rui_min[i + 1] = min(rui_min[i], rui[i + 1])
    q = deque()
    cnt = 0
    flag = False
    l = 0
    for r in range(N):
        q.append(r)
        if S[r] == "o":
            cnt += 1
        while len(q) and cnt - (1 if S[q[0]] == "o" else 0) >= K:
            l = q.popleft()
            if S[l] == "o":
                cnt -= 1
        if cnt >= K and rui[r + 1] - rui_min[l + 1] >= 0:
            flag = True
    return flag


ok, ng = 0, 1

while abs(ng - ok) > (1 / 10**7):
    mid = (ok + ng) / 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
