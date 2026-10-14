N, Q = map(int, input().split())

A = [0 for i in range(N)]
for _ in range(Q):
    query = input()
    if query[0] == "1":
        _, a, b, v = map(int, query.split())
        A[a - 1] -= v
        A[b - 1] += v
    elif query[0] == "2":
        _, x, l, r = map(int, query.split())
        ans = 0
        for i in range(l - 1, r):
            if A[i] > A[x - 1]:
                ans += 1
        print(ans)
    else:
        _, l, r, v = map(int, query.split())
        for i in range(l - 1, r):
            A[i] += v
