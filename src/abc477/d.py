from bisect import bisect_left

N, Q = map(int, input().split())

queries = [input() for qi in range(Q)]
times = [0]
colors = ["a"]
one_queries = []
for qi in range(Q):
    query = queries[qi]
    if query[0] == "1":
        _, X = map(int, query.split())
        one_queries.append((qi + 1, X - 1))
    else:
        _, C = query.split()
        times.append(qi + 1)
        colors.append(C)

ttc = [[0, 0, "a"] for i in range(N)]
for time, X in one_queries:
    if ttc[X][0] == 0:
        # タイルがない状態からある状態に移行するとき
        bl = bisect_left(times, time)
        ttc[X][0] = 1
        ttc[X][1] = time
        ttc[X][2] = colors[bl - 1]
    else:
        # タイルを外すとき
        ttc[X][0] = 0
        ttc[X][1] = time
    print(ttc)

ans = []

for i in range(N):
    if ttc[i][0] == 1:
        ans.append(ttc[i][2])
    else:
        bl = bisect_left(times, ttc[i][1])
        if bl == len(times):
            ans.append(ttc[i][2])
        else:
            ans.append(colors[-1])

print("".join(ans))

ans1 = ["a"] * N
huta = [0 for i in range(N)]
for qi in range(Q):
    query = queries[qi]
    if query[0] == "1":
        _, X = map(int, query.split())
        huta[X - 1] = (huta[X - 1] + 1) % 2
    else:
        _, C = query.split()
        for i in range(N):
            if huta[i]:
                continue
            ans1[i] = C

print("".join(ans1))
