from atcoder.twosat import TwoSAT


N, M = map(int, input().split())
AD = [list(map(int, input().split())) for _ in range(N)]
UV = [list(map(int, input().split())) for _ in range(M)]
UV = [(u - 1, v - 1) for u, v in UV]

ok = 0
ng = 10**10 + 10


def two_sat_setup(ts, k):
    global AD, UV
    for u, v in UV:
        for x, y in [
            [False, False],
            [True, False],
            [False, True],
            [True, True],
        ]:
            tu = AD[u][0] + (AD[u][1] if x else 0)
            tv = AD[v][0] + (AD[v][1] if y else 0)
            if abs(tu - tv) < k:
                ts.add_clause(u, not x, v, not y)
    return ts


def is_ok(k):
    global N, M, UV, two_sat_setup
    two_sat = TwoSAT(N)
    two_sat = two_sat_setup(two_sat, k)
    return two_sat.satisfiable()


while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid


ans = [-1 for _ in range(N)]
for i in range(N):
    check_two_sat = TwoSAT(N)
    check_two_sat = two_sat_setup(check_two_sat, ok)
    for j in range(N):
        if ans[j] == 0:
            check_two_sat.add_clause(j, False, j, False)
    check_two_sat.add_clause(i, False, i, False)
    flag = check_two_sat.satisfiable()
    if not flag:
        ans[i] = 1
    else:
        ans[i] = 0

print(ok)
print(*ans, sep="")
