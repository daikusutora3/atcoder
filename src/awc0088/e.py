from collections import defaultdict
from math import isqrt

N, Q = map(int, input().split())
S = input()
queries = [tuple(map(int, input().split())) for _ in range(Q)]
queries = [(q[0] - 1, q[1]) for q in queries]

B = max(1, isqrt(N))

mo_queries = []
for i, (l, r) in enumerate(queries):
    mo_queries.append((l, r, i))

mo_queries.sort(key=lambda x: (x[0] // B, -x[1] if (x[0] // B) % 2 else x[1]))

cur_l, cur_r = 0, -1
cur_ans = 0
ans = [0 for i in range(Q)]
d = defaultdict(int)
rui = [0 for i in range(N + 1)]

for i in range(N):
    rui[i + 1] += rui[i] + (1 if S[i] == "W" else -1)


def add(i):
    global cur_ans, d, rui
    cur_ans += d[rui[i]] + d[rui[i] - 1] + d[rui[i] + 1]
    d[rui[i]] += 1
    # print("ADD")
    # print(f"{cur_l}~{cur_r}: {cur_ans}")


def remove(i):
    global cur_ans, d, A
    d[rui[i]] -= 1
    cur_ans -= d[rui[i]] + d[rui[i] - 1] + d[rui[i] + 1]
    # print("REMOVE")
    # print(f"{cur_l}~{cur_r}: {cur_ans}")


for l, r, qi in mo_queries:
    # 左端を広げる
    while cur_l > l:
        cur_l -= 1
        add(cur_l)

    # 右端を広げる
    while cur_r < r:
        cur_r += 1
        add(cur_r)

    # 左端を縮める
    while cur_l < l:
        remove(cur_l)
        cur_l += 1

    # 右端を縮める
    while cur_r > r:
        remove(cur_r)
        cur_r -= 1

    # print(f"区間: {A[l : r + 1]}, ans: {cur_ans}")
    # print(d)
    ans[qi] = cur_ans

for i in range(Q):
    print(ans[i])
