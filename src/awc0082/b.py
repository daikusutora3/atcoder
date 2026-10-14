N, K, M, X = map(int, input().split())
if M != 0:
    Y = list(map(int, input().split()))

A = [0 for i in range(N)]

for _ in range(K):
    if X & 1:
        break
    else:
        X = X >> 1
        X |= 2 ** (N - 1)
    # print(bin(X))

for i in range(N):
    cnt = 0
    if (X >> i) & 1:
        cnt += 1
    for j in range(M):
        if (Y[j] >> i) & 1:
            cnt += 1
    A[i] = cnt

ruiA = [0 for i in range(N + 1)]

for i in range(N):
    ruiA[i + 1] = ruiA[i] + A[i] * pow(2, i)


ans = 0

for i in range(1, N):
    left = ruiA[i]
    right = (ruiA[N] - ruiA[i]) // pow(2, i)
    ans = max(ans, left + right)


print(ans)
