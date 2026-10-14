from bisect import bisect_left


N, Q = map(int, input().split())
YP = [list(map(int, input().split())) for i in range(N)]

YP.sort()
Y = [yp[0] for yp in YP]
P_rui = [0 for i in range(N + 1)]
for i in range(N):
    P_rui[i + 1] += P_rui[i] + YP[i][1]
for _ in range(Q):
    L = int(input())
    bl = bisect_left(Y, L)
    print(P_rui[N] - P_rui[bl])
