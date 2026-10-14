from atcoder.fenwicktree import FenwickTree

N = int(input())
PV = [list(map(int, input().split())) for i in range(N)]
PV.sort()
V = [PV[i][1] for i in range(N)]
S = sorted(list(set(V)))
ranking = {x: i + 1 for i, x in enumerate(S)}
V_zaatsu = []
for v in V:
    V_zaatsu.append(ranking[v])

fenwick_tree = FenwickTree(N)

ans = 0
for i in range(N):
    ans += fenwick_tree.sum(V_zaatsu[i], N)
    fenwick_tree.add(V_zaatsu[i] - 1, 1)

print(ans)
