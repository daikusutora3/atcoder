N = int(input())


def is_ok_d(n, k):
    global N
    seki = 1
    na = 1
    for _ in range(n):
        seki *= na
        na += k
        if seki > N:
            break
    return seki <= N


def is_ok_a1(n, a1):
    global N
    seki = 1
    na = a1
    for _ in range(n):
        seki *= na
        na += 1
        if seki > N:
            break
    return seki <= N


def is_ok(n, a1, k):
    global N
    seki = 1
    na = a1
    for _ in range(n):
        seki *= na
        na += k
        if seki > N:
            break
    # print(n, a1, k, seki, seki <= N)
    return seki <= N


ans = 0
for n in range(3, 21):
    ng_d = 10**9
    ok_d = 0
    while ng_d - ok_d > 1:
        mid = (ok_d + ng_d) // 2
        if is_ok_d(n, mid):
            ok_d = mid
        else:
            ng_d = mid

    ng_a1 = 10**9
    ok_a1 = 0
    while ng_a1 - ok_a1 > 1:
        mid = (ok_a1 + ng_a1) // 2
        if is_ok_a1(n, mid):
            ok_a1 = mid
        else:
            ng_a1 = mid
    for a1 in range(1, ng_a1):
        seki = 1
        ok_d = 0
        while ng_d - ok_d > 1:
            mid = (ok_d + ng_d) // 2
            if is_ok(n, a1, mid):
                ok_d = mid
            else:
                ng_d = mid
        ans += ok_d

print(ans)
