from collections import deque


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
    for h in range(1, H + 1 - i):
        if K == 0:
            cnt0 = 0
            for j in range(W):
                ijh = rui_get(i, j, h, 1)
                if ijh == 0:
                    cnt0 += 1
                    ans += cnt0
                else:
                    cnt0 = 0
            continue
        queue = deque()
        now = 0
        cnt = 0
        for j in range(W):
            queue.append(j)
            ijh = rui_get(i, j, h, 1)
            now += ijh

            while now > K:
                oj = queue.popleft()
                oijh = rui_get(i, oj, h, 1)
                now -= oijh
                cnt = 0

            while queue and now == K:
                oj = queue[0]
                oijh = rui_get(i, oj, h, 1)

                if oijh != 0:
                    break

                queue.popleft()
                cnt += 1

            if now == K:
                ans += 1 + cnt

print(ans)
