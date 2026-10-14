N, K = map(int, input().split())
for i in range(N):
    print((i - K) % N + 1)
