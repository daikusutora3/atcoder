N, D = map(int, input().split())

XP = [list(map(int, input().split())) for i in range(N)]
XP.sort()

r = -1
s = 0
ans = 0
for l in range(N):
    while r + 1 <= l or (r + 1 < N and XP[r + 1][0] < XP[l][0] + D):
        # print("+", XP[r + 1])
        s += XP[r + 1][1]
        r += 1
    # print(f"{XP[l][0]}~{XP[l][0] + D}: {s}")
    ans = max(ans, s)
    s -= XP[l][1]
    # print("-", XP[l])

# print(sum([p for x, p in XP]))
print(sum([p for x, p in XP]) - ans)
