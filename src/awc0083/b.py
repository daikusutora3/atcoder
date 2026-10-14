N, Q = map(int, input().split())
H = list(map(int, input().split()))

for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, x, h = map(int, query.split())
        H[x - 1] = h
    else:
        _, a, b = map(int, query.split())
        ans = 0
        tmp = float("inf")
        for p in range(a - 1, b):
            Lp = 0
            Rp = 0
            for l in range(0, p):
                Lp = max(Lp, H[l] / (p - l))
            for r in range(p + 1, N):
                Rp = max(Rp, H[r] / (r - p))
            if tmp > 1 + Lp + Rp:
                tmp = 1 + Lp + Rp
                ans = p
        print(ans + 1)
