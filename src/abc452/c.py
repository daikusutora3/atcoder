N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
S = [input() for _ in range(M)]


check = [[[0 for k in range(26)] for j in range(11)] for i in range(11)]
for i in range(M):
    for j, s in enumerate(S[i]):
        check[len(S[i])][j][ord(s) - ord("a")] = 1

# print(check)
for _ in range(M):
    if len(S[_]) != N:
        print("No")
        continue
    flag = True
    for i, s in enumerate(S[_]):
        if check[AB[i][0]][AB[i][1] - 1][ord(s) - ord("a")] == 0:
            flag = False
    print("Yes" if flag else "No")
