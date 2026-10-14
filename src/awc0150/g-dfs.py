N, Q = map(int, input().split())

T = [x - 1 for x in map(int, input().split())]

# vec[v]
#   0より大きい : vから始めて訪れる頂点数が確定済み
#   0           : まだ未訪問
#   0より小さい : 現在探索中。-何番目に訪れたか
vec = [0] * N

for i in range(N):
    if vec[i] != 0:
        continue

    num = i
    que = []

    # 未訪問の頂点を一本道に進んでいく
    while vec[num] == 0:
        que.append(num)
        # 現在の探索で何番目に訪れたかを負数で記録
        vec[num] = -len(que)
        num = T[num]

    # すでに答えが確定している頂点に到着した場合
    # vec[num] + 1 が1つ手前の答えになる
    value = vec[num] + 1

    # vec[num] <= 0
    # → 今回の探索中の頂点に戻ってきた
    # → 閉路を発見
    if value <= 0:
        # 閉路長
        value = len(que) + value

        # 閉路上の頂点を全部「閉路長」にする
        while que[-1] != num:
            vec[que[-1]] = value
            que.pop()

    # 残りを後ろから処理
    #
    # 閉路の場合:
    #   閉路上は cycle_len
    #   その手前は cycle_len + 1, cycle_len + 2, ...
    #
    # 計算済み頂点にぶつかった場合:
    #   vec[num] + 1, vec[num] + 2, ...
    while que:
        vec[que[-1]] = value
        que.pop()
        value += 1


for _ in range(Q):
    S = int(input()) - 1
    print(vec[S])
