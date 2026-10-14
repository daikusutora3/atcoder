H, W, K = map(int, input().split())
grid = [input() for i in range(H)]
rui = [[0 for j in range(W + 1)] for i in range(H + 1)]


for i in range(H):
    for j in range(W):
        if grid[i][j] == "1":
            rui[i + 1][j + 1] = 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        rui[i][j] += rui[i - 1][j] + rui[i][j - 1] - rui[i - 1][j - 1]


def rui_get(i, j, h, w):
    global rui
    return rui[i + h][j + w] - rui[i][j + w] - rui[i + h][j] + rui[i][j]


ans = 0

for i in range(H):
    for j in range(W):
        for h in range(1, H + 1 - i):

            def is_ok1(k):
                global h, i, j, K
                return rui_get(i, j, h, k) >= K

            ok1 = W - j
            ng1 = 0

            while ok1 - ng1 > 1:
                mid = (ok1 + ng1) // 2
                if is_ok1(mid):
                    ok1 = mid
                else:
                    ng1 = mid

            def is_ok2(k):
                global h, i, j, K
                return rui_get(i, j, h, k) <= K

            ok2 = 0
            ng2 = W - j + 1

            while ng2 - ok2 > 1:
                mid = (ok2 + ng2) // 2
                if is_ok2(mid):
                    ok2 = mid
                else:
                    ng2 = mid

            if rui_get(i, j, h, ok1) == K:
                ans += ok2 - ok1 + 1

print(ans)
