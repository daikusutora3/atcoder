N, M = map(int, input().split())
T = N * M
SD = [list(map(int, input().split())) for i in range(M)]

dp = [[False for bit in range(2**M)] for i in range(N)]
ndp = [[False for bit in range(2**M)] for i in range(N)]

dp[0][0] = True
pos = [SD[i][0] - 1 for i in range(M)]
for t in range(1, T + 1):
    for i in range(M):
        pos[i] = (pos[i] + SD[i][1]) % N
    for a in range(N):
        for bit in range(2**M):
            nbit = bit
            for i in range(M):
                if a == pos[i]:
                    nbit |= 1 << i
            ndp[a][nbit] |= dp[a][bit]
            if a + 1 < N:
                nbit = bit
                for i in range(M):
                    if a + 1 == pos[i]:
                        nbit |= 1 << i
                ndp[a + 1][nbit] |= dp[a][bit]
            if 0 <= a - 1:
                nbit = bit
                for i in range(M):
                    if a - 1 == pos[i]:
                        nbit |= 1 << i
                ndp[a - 1][nbit] |= dp[a][bit]
    dp = ndp
    ndp = [[False for bit in range(2**M)] for i in range(N)]
    is_ok = False
    for a in range(N):
        is_ok |= dp[a][2**M - 1]
    if is_ok:
        break


print(t)
