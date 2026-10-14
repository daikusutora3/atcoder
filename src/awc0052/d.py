N, M = map(int, input().split())
Scan = [list(map(int, input().split())) for i in range(M)]

ans = 100
# どの端末が感染しているかの集合
for bit in range(2**N):
    ok = True
    for i in range(M):
        K, R = Scan[i][0], Scan[i][-1]
        osen = False
        for j in range(K):
            # bitのS_i_jが汚染されているかどうかを見る
            if bit >> (Scan[i][j + 1] - 1) & 1:
                osen = True
        if (osen and R == 1) or (not osen and R == 0):
            pass
        else:
            ok = False
    if ok:
        cnt = 0
        while bit > 0:
            if bit & 1:
                cnt += 1
            bit >>= 1
        ans = min(ans, cnt)

print(ans)
