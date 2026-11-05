S = [input() for i in range(5)]

ans = float("inf")

# 各行(横方向を見る)
for i in range(5):
    ans = min(ans, 5 - S[i].count("o"))

# 各列(縦方向を見る)
for j in range(5):
    cnt = 0
    for i in range(5):
        if S[i][j] == "o":
            cnt += 1
    ans = min(ans, 5 - cnt)

# 斜め
cnt = 0
for i in range(5):
    if S[i][i] == "o":
        cnt += 1
ans = min(ans, 5 - cnt)

cnt = 0
for i in range(5):
    if S[4 - i][i] == "o":
        cnt += 1
ans = min(ans, 5 - cnt)

print(ans)
