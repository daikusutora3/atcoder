# bfs

## Summary

- 重みなしグラフで、各頂点について始点配列の中の最も近い始点からの最短距離を求める。
- `graph[v]` に隣接頂点を持つ 0-indexed の隣接リストと、始点配列 `starts` を渡す。各始点は有効な頂点番号とする。
- 有向・無向グラフ、多重辺、自己ループ、非連結グラフに対応する。有向グラフでは始点から辺の向きに沿って進む距離を求める。
- 始点の距離は `0`、どの始点からも到達できない頂点は `-1`。
- 始点の重複を許し、同じ頂点をキューへ重複追加しない。`starts` が空なら全頂点 `-1`。空グラフには空の始点配列を渡す。
- `visited` を渡すと、あらかじめ `True` の頂点を除いたグラフで探索する。始点でも `True` なら除外し、今回探索しなかった頂点の距離は `-1`。
- `visited` は長さ `V` の bool 配列とし、発見した頂点を直接 `True` に更新する。再利用すると前回探索した頂点にも入らなくなる。省略時は呼び出しごとに新規作成する。

## Functions

| Function | Input | Output | Complexity |
| --- | --- | --- | --- |
| `bfs(graph, starts, visited=None)` | 隣接リスト `graph: list[list[int]]`、始点配列 `starts: list[int]`、任意の `visited: list[bool]` | 距離配列 `dist: list[int]` | 時間 `O(V + E + K)`、追加空間 `O(V)` |

`V` は頂点数、`E` は隣接リストの要素数の合計、`K` は重複を含む始点数。無向辺は両方向の要素として数える。

## Usage

```python
from library.graph.bfs import bfs

graph = [[1], [0, 2], [1, 3], [2], []]

# 単一始点
assert bfs(graph, [0]) == [0, 1, 2, 3, -1]

# 多始点：0 または 3 からの最短距離
assert bfs(graph, [0, 3]) == [0, 1, 1, 0, -1]

# 重複・空配列
assert bfs(graph, [0, 0, 3]) == [0, 1, 1, 0, -1]
assert bfs(graph, []) == [-1, -1, -1, -1, -1]
assert bfs([], []) == []
```

木の中心を通らずに枝ごとに探索する例:

```python
graph = [[1, 2], [0, 3], [0, 4], [1], [2]]
visited = [False] * len(graph)
visited[0] = True  # 中心を通行禁止にする

assert bfs(graph, [1], visited) == [-1, 0, -1, 1, -1]
assert visited == [True, True, False, True, False]
assert bfs(graph, [2], visited) == [-1, -1, 0, -1, 1]
assert visited == [True] * len(graph)
assert bfs(graph, [0], visited) == [-1] * len(graph)
```

距離配列は毎回長さ `V` で初期化するため、小さな枝を探索する場合も1回につき時間 `O(V)` はかかる。枝数が多い木で繰り返し呼ぶと合計 `O(V²)` になり得るので、ABC482 E の枝ごとの探索へそのまま置き換える際は注意する。

連結な重みなし無向木の直径の長さは、BFS を2回行うと求められる。

```python
graph = [[1], [0, 2], [1, 3], [2]]  # 木の隣接リスト
dist = bfs(graph, [0])
s = max(range(len(graph)), key=dist.__getitem__)
dist = bfs(graph, [s])
diameter = max(dist)  # 辺数。この例では 3。
```

一般のグラフでは BFS 2回で直径が求まるとは限らない。この API は親配列・経路を返さない。

## References

- [ABC482 E の解答](../../src/abc482/e.py): BFS による距離探索を切り出し、多始点へ一般化した。
- [cp-algorithms: Breadth First Search](https://cp-algorithms.com/graph/breadth-first-search.html): BFS の距離更新とキューによる探索手順を確認した。

## Related

- 問題: [ABC482 E](https://atcoder.jp/contests/abc482/tasks/abc482_e)
- 自分の解答: [../../src/abc482/e.py](../../src/abc482/e.py)
