N, Q = map(int, input().split())
S = list(map(int, input().split()))
C = list(map(int, input().split()))

closed = [False for i in range(N)]
for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, l, r, v = map(int, query.split())
        for i in range(l - 1, r):
            C[i] += v
    if query[0] == "2":
        _, x = map(int, query.split())
        closed[x - 1] = True
    if query[0] == "3":
        _, l, r = map(int, query.split())
        ans = 0
        for i in range(l - 1, r):
            if closed[i] or C[i] > 0:
                continue
            ans += S[i]
        print(ans)
