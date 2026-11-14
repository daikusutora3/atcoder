N, Q = map(int, input().split())
ans = [i + 1 for i in range(N)]
K = list(map(int, input().split()))

for q in range(Q):
    k = K[q]
    nans = ans[:]
    for i in range(k):
        nans[i] = -ans[k - 1 - i]
    ans = nans

print(*ans, sep="\n")
