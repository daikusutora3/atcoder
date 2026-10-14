from atcoder.dsu import DSU

N, Q = map(int, input().split())
dsu = DSU(N)

for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, a, b = map(int, query.split())
        dsu.merge(a - 1, b - 1)
    else:
        _, x = map(int, query.split())
        print(dsu.size(x - 1))
