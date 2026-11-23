from atcoder.dsu import DSU

N = int(input())
uf = DSU(N)
C = list(map(int, input().split()))
cnt = [0 for i in range(N)]
now = 0
for i in range(N):
    if 0 < i and C[i - 1] == C[i]:
        uf.merge(i - 1, i)
        now += 1
        cnt[i] = now
    else:
        now = 0
        cnt[i] = now


for i in range(N):
    if uf.leader(i) == uf.leader(0):
        print(uf.size(i) - cnt[i], end=" ")
    elif uf.leader(i) == uf.leader(N - 1):
        print(cnt[i] + 1)
    else:
        print(min(cnt[i] + 1, uf.size(i) - cnt[i]), end=" ")
