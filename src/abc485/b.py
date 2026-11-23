import sys

N, M = map(int, input().split())
S = [input() for i in range(N)]

for i in range(N):
    if S[i].count("x") == M:
        print("Faucet", i + 1)
        sys.exit()

for j in range(M):
    if S[0][j] == "x":
        print("Drain", j + 1)
        sys.exit()
