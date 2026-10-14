N, L, T = map(int, input().split())

for _ in range(N):
    X, V = map(int, input().split())
    x = X + V * T
    if (x // L) % 2 == 1:
        print(L - (X + V * T) % L)
    else:
        print((X + V * T) % L)
