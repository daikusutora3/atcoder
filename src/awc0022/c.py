N, M, K, T = map(int, input().split())
B = set(map(int, input().split()))

ruiseki = [0 for i in range(N + 1)]
for i in range(N):
    if i + 1 in B:
        ruiseki[i + 1] = ruiseki[i] + 1
    else:
        ruiseki[i + 1] = ruiseki[i]

for _ in range(K):
    L, R = map(int, input().split())
    if ruiseki[R] - ruiseki[L - 1] >= T:
        print("YES")
    else:
        print("NO")
