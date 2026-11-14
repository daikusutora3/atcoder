N, K = map(int, input().split())
A = list(map(int, input().split()))


# １番目: ２分探索
def is_ok(N, K, A, k):
    INF = float("inf")
    cnt = [k // A[i] if A[i] != 0 else INF for i in range(N)]
    need = INF
    p = -1
    res = []
    flag = True
    for i in range(N):
        if p == -1:
            need = min(need - 1, cnt[i])
        elif i - p <= cnt[i]:
            need = need - 1
        else:
            need = min(need - 1, cnt[i])
            flag = True
        if need <= 0:
            p = i
            need = INF
            res.append(i)
            flag = False
    if flag:
        res.append(N - 1)
    return len(res) <= K


ok = 10**15
ng = -1

while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_ok(N, K, A, mid):
        ok = mid
    else:
        ng = mid

print(ok)
