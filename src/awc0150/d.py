N, K, Q = map(int, input().split())
S = [[int(s) for s in list(input())] for i in range(N)]

for _ in range(Q):
    R, C = map(int, input().split())
    sub_S = [[-1 for j in range(K)] for i in range(K)]
    for i in range(K):
        for j in range(K):
            sub_S[i][j] = S[i + R - 1][j + C - 1]
    for i, row in enumerate(zip(*sub_S[::-1])):
        for j, x in enumerate(row):
            S[i + R - 1][j + C - 1] = x


for s in S:
    print(*s, sep="")
