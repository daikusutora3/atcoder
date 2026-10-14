import itertools


N, K = map(int, input().split())
LR = [list(map(int, input().split())) for i in range(N)]
S = sorted(list(set(itertools.chain.from_iterable(LR))))
ranking = {x: i for i, x in enumerate(S)}
LR_zaatu = []
for lr in LR:
    l, r = lr
    LR_zaatu.append([ranking[l], ranking[r]])

imos = [0 for i in range(len(ranking))]
for i in range(N):
    l, r = LR_zaatu[i]
    imos[l] += 1
    imos[r] -= 1

for i in range(len(ranking) - 1):
    imos[i + 1] += imos[i]

ans = 0
for i in range(len(ranking) - 1):
    if imos[i] >= K:
        ans += S[i + 1] - S[i]

print(ans)
