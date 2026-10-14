from numpy import base_repr


N, K = map(int, input().split())
for _ in range(K):
    # N進数, 10進数
    base_10 = int(str(N), 8)
    N = base_repr(base_10, 9).replace("8", "5")

print(N)
