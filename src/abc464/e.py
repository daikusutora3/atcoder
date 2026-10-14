H, W, Q = map(int, input().split())
rui = [[-float("inf") for j in range(W + 1)] for i in range(H + 1)]


RCX = [[H, W, "A"]] + [input().split() for i in range(Q)]
for time in range(Q + 1):
    R, C, X = RCX[time]
    R = int(R)
    C = int(C)
    rui[R][C] = time


for i in range(H + 1):
    for j in range(W - 1, -1, -1):
        rui[i][j] = max(rui[i][j], rui[i][j + 1])


for j in range(W + 1):
    for i in range(H - 1, -1, -1):
        rui[i][j] = max(rui[i][j], rui[i + 1][j])


for i in range(H):
    res = []
    for j in range(W):
        res.append(RCX[rui[i + 1][j + 1]][2])
    print("".join(res))
