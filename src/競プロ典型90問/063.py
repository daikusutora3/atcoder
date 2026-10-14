from collections import defaultdict


H, W = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(H)]

ans = 0
for bit in range(2**H):
    # どの行を取りますか
    check = []
    for i in range(H):
        if bit >> i & 1:
            check.append(i)
    if len(check) == 0:
        continue
    d = defaultdict(int)
    # 各列に対して取る行の値が全部同じかを見る
    for j in range(W):
        flag = True
        for i in check:
            if grid[i][j] != grid[check[0]][j]:
                flag = False
        if flag:
            d[grid[check[0]][j]] += 1
    if len(d.values()) > 0:
        ans = max(ans, max(d.values()) * len(check))

print(ans)
