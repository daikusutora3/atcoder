def compress(values):
    """(comp, vals, idx) を返す。

    comp: values と同じ順序・長さの圧縮後リスト
    vals: values に登場する値を昇順に重複除去したリスト
    idx: 元の値から圧縮後 index への辞書

    計算量: 期待時間 O(N + U log(U + 1))、空間 O(N + U)。N は入力数、U は異なる値数。

    Source: https://github.com/daikusutora3/atcoder
    """
    vals = sorted(set(values))
    idx = {x: i for i, x in enumerate(vals)}
    comp = [idx[x] for x in values]
    return comp, vals, idx


H, W, N, Q = map(int, input().split())

RC = [list(map(int, input().split())) for i in range(N)]
queries = [list(map(int, input().split())) for _ in range(Q)]

R = []
C = []
for i in range(N):
    R.append(RC[i][0])
    C.append(RC[i][1])

for i in range(Q):
    q, a, b = queries[i]
    if q == 1:
        R.append(a)
        R.append(b)
    else:
        C.append(a)
        C.append(b)

Rcomp = compress(R)
Ccomp = compress(C)

Rrui = [0 for i in range(len(Rcomp[1]) + 1)]
Crui = [0 for i in range(len(Ccomp[1]) + 1)]

for r, c in RC:
    Rrui[Rcomp[2][r] + 1] += 1
    Crui[Ccomp[2][c] + 1] += 1

for i in range(len(Rcomp[1])):
    Rrui[i + 1] += Rrui[i]

for j in range(len(Ccomp[1])):
    Crui[j + 1] += Crui[j]

for _ in range(Q):
    q, a, b = queries[_]
    if q == 1:
        print(Rrui[Rcomp[2][b] + 1] - Rrui[Rcomp[2][a]])
    else:
        print(Crui[Ccomp[2][b] + 1] - Crui[Ccomp[2][a]])
