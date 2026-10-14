N, K = map(int, input().split())
A = list(map(int, input().split()))


def is_ok(k):
    cnt = 0
    for i in range(N):
        if A[i] < k:
            cnt += (k - A[i] + i) // (i + 1)  # ceil((k - A[i]) / (i + 1))

            # cnt が K を超えたら、それ以上正確に数えなくてよい
            if cnt > K:
                return False

    return cnt <= K


# 指数探索で ng を探す
ok = 0
ng = 1

while is_ok(ng):
    ok = ng
    ng *= 2


while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
