N = int(input())

dp = [0 for i in range(3)]
ndp = [-float("inf") for i in range(3)]

for i in range(N):
    ndp = [-float("inf") for i in range(3)]
    abc = list(map(int, input().split()))
    for ac in range(3):
        for nac in range(3):
            if ac == nac:
                continue
            ndp[nac] = max(ndp[nac], dp[ac] + abc[nac])
    dp = ndp

print(max(dp))
