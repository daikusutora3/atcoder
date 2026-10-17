S = [input() for i in range(2)]


ans = False
for i in range(2):
    for j in range(2):
        if S[i][j] == "A":
            for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                ni = di + i
                nj = dj + j
                if not (0 <= ni < 2 and 0 <= nj < 2):
                    continue
                if S[ni][nj] == "D":
                    ans = True

if ans:
    print("Yes")
else:
    print("No")
