from itertools import product


N, Q = map(int, input().split())
xyzw = [list(map(int, input().split())) for i in range(Q)]
ans = 1
mod = 10**9 + 7

for k in range(60):
    cnt = 0
    # k桁目の各A[i]のbitについて全探索
    for bit in product((0, 1), repeat=N):
        flag = True
        for q in range(Q):
            x, y, z, w = xyzw[q]
            x, y, z = x - 1, y - 1, z - 1
            if bit[x] | bit[y] | bit[z] != ((w >> k) & 1):
                flag = False
            # print(bit[x], bit[y], bit[z], ((w >> k) & 1))
        # print(flag, bit, ((w >> k) & 1))
        if flag:
            cnt += 1
    ans *= cnt
    ans %= mod

print(ans)
