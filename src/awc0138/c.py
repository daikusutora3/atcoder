N, K = map(int, input().split())

AB = [list(map(int, input().split())) for i in range(N)]
r = -1
cost = 0
manzoku = 0
ans = 0
for l in range(N):
    while r + 1 <= l or (r + 1 < N and AB[r + 1][1] + cost <= K):
        cost += AB[r + 1][1]
        manzoku += AB[r + 1][0]
        r += 1
    if l == r and cost > K:
        pass
    else:
        ans = max(ans, manzoku)
    cost -= AB[l][1]
    manzoku -= AB[l][0]

print(ans)
