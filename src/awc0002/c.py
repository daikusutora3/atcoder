N, M = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(N)]

def is_ok(d):
    res = True
    global AB, N, M
    for i in range(N):
        a, b = AB[i]
        if not(M <= a + b*d):
            res = False
    return res

        

ng = -1
ok = 10**9+1

while ok - ng > 1:
    mid = (ok+ng)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
        

print(ok)