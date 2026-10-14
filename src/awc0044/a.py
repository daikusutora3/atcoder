N, M = map(int, input().split())

for i in range(N):
    C, S = map(int, input().split())
    print(min(C - S, M) + S)
    M -= min(C - S, M)
