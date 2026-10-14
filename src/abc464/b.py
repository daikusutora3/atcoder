from functools import lru_cache


H, W = map(int, input().split())

C = [input() for i in range(H)]


@lru_cache(maxsize=None)
def is_row_white(i):
    global W, C
    res = True
    for j in range(W):
        if C[i][j] == "#":
            res = False
    return res


@lru_cache(maxsize=None)
def is_column_white(j):
    global H, C
    res = True
    for i in range(H):
        if C[i][j] == "#":
            res = False
    return res


skip_i = set()

for i in range(H):
    if is_row_white(i):
        skip_i.add(i)
    else:
        break
for i in range(H - 1, -1, -1):
    if is_row_white(i):
        skip_i.add(i)
    else:
        break
skip_j = set()

for j in range(W):
    if is_column_white(j):
        skip_j.add(j)
    else:
        break
for j in range(W - 1, -1, -1):
    if is_column_white(j):
        skip_j.add(j)
    else:
        break

for i in range(H):
    if i in skip_i:
        continue
    res = []
    for j in range(W):
        if j in skip_j:
            continue
        res.append(C[i][j])
    if len(res):
        print("".join(res))
