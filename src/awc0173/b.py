H, W = map(int, input().split())
S = [input() for i in range(H)]
ans = 0

for j in range(W):
    flag = True
    for i in range(H):
        if S[i][j] == "#":
            flag = False
    if flag:
        ans += 1

print(ans)
