def is_ok(k, A, B):
    flag = True
    for i in range(max(1, k // 2 - 5), k // 2 + 6):
        # １回目の大会で高橋くんを無視してi番目の順位
        # 実際の順位x
        x = i
        if A <= x:
            x += 1
        y = k - i + 1
        if B <= y:
            y += 1
        if x * y >= A * B:
            flag = False
    return flag


def solve():
    A, B = map(int, input().split())
    if A < B:
        A, B = B, A
    ok = 0
    ng = 10**10
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, A, B):
            ok = mid
        else:
            ng = mid
    print(ok)


T = int(input())
for _ in range(T):
    solve()
