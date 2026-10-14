N, P, K = map(int, input().split())

A = [list(map(int, input().split())) for i in range(N)]


def f(k):
    global N, P, K, A
    dist = [[float("inf") for i in range(N)] for i in range(N)]
    for i in range(N):
        dist[i][i] = 0

    for i in range(N):
        for j in range(N):
            dist[i][j] = A[i][j] if A[i][j] != -1 else k

    for k in range(N):  # 中継点
        for i in range(N):  # 始点
            for j in range(N):  # 終点
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if dist[i][j] <= P:
                cnt += 1
    return cnt


def is_ok1(k):
    return f(k) >= K


ok1, ng1 = 0, 10**15

while ng1 - ok1 > 1:
    mid = (ok1 + ng1) // 2
    if is_ok1(mid):
        ok1 = mid
    else:
        ng1 = mid


def is_ok2(k):
    return f(k) >= K + 1


ok2, ng2 = 0, 10**15

while ng2 - ok2 > 1:
    mid = (ok2 + ng2) // 2
    if is_ok2(mid):
        ok2 = mid
    else:
        ng2 = mid


print("Infinity" if ok1 - ok2 >= 10**14 else ok1 - ok2)
