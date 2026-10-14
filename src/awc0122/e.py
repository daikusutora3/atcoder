from math import isqrt

N, K, Q = map(int, input().split())
LRX = [list(map(int, input().split())) for i in range(N)]

# 変換器にある値iを入れたときの出力を入れる配列
A = [-1 for i in range(K)]
for k in range(1, K + 1):
    now = k
    for i in range(N):
        L, R, X = LRX[i]
        if L <= now <= R:
            now = X
    A[k - 1] = now

queries = [tuple(map(int, input().split())) for _ in range(Q)]
queries = [(q[0] - 1, q[1] - 1) for q in queries]

B = max(1, isqrt(K))

mo_queries = []
for i, (l, r) in enumerate(queries):
    mo_queries.append((l, r, i))

mo_queries.sort(key=lambda x: (x[0] // B, -x[1] if (x[0] // B) % 2 else x[1]))

cur_l, cur_r = 0, -1
d = [0 for i in range(K + 1)]
cur_ans = 0
ans = [0 for i in range(Q)]


def add(i):
    global cur_ans, d, A
    if d[A[i]] == 0:
        cur_ans += 1
    d[A[i]] += 1


def remove(i):
    global cur_ans, d, A
    d[A[i]] -= 1
    if d[A[i]] == 0:
        cur_ans -= 1


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

    # print(f"区間: {A[l : r + 1]}, ans: {d}")
    # print(d)
    ans[qi] = cur_ans

for i in range(Q):
    print(ans[i])
