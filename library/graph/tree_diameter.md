# tree_diameter

## Summary

- 重みなし無向木の直径の長さ・経路と、木の中心を求める。
- 入力は 0-indexed の隣接リスト。空でない連結な単純無向木を渡し、各辺を両方向に登録する。入力の検査は行わない。
- 直径の長さは辺数、経路は両端を含む頂点列。複数の直径がある場合はそのうち1本を返し、向きは未規定。
- 中心は、全頂点への距離の最大値（離心度）が最小となる頂点。直径の辺数が偶数なら1頂点、奇数なら隣り合う2頂点。
- 重心とは異なる。重心は頂点を除去した後の連結成分の大きさで定義する。

## Functions

| Function | Output | Complexity |
| --- | --- | --- |
| `tree_diameter(graph)` | `(diameter, path): tuple[int, list[int]]` | 時間 `O(N)`、追加空間 `O(N)` |
| `tree_centers(graph)` | 中心の頂点配列 `list[int]` | 時間 `O(N)`、追加空間 `O(N)` |

`N` は頂点数。1頂点の木では `(0, [0])` と `[0]` を返す。BFS を2回行い、2回目の親配列で経路を復元する。単独で貼り付けて使え、既存の BFS ライブラリへの依存はない。`tree_centers` を貼る場合は `tree_diameter` も必要。

## Usage

```python
from library.graph.tree_diameter import tree_diameter, tree_centers

graph = [[1], [0, 2], [1, 3], [2]]
diameter, path = tree_diameter(graph)
assert diameter == 3
assert path in ([0, 1, 2, 3], [3, 2, 1, 0])
assert set(tree_centers(graph)) == {1, 2}

# 直径経路をすでに取得している場合は再探索せず中心を取り出せる。
centers = path[diameter // 2 : diameter // 2 + 1 + diameter % 2]
assert set(centers) == {1, 2}
```

ABC482 E の解答のように各辺へ補助頂点を1個挿入すると、距離と直径の辺数は2倍になり、中心は必ず1頂点になる。

```python
# 元の木が 0 -- 1 の場合、補助頂点 2 を挿入する。
graph = [[2], [2], [0, 1]]
diameter, path = tree_diameter(graph)
center = path[diameter // 2]
assert diameter == 2 and center == 2
```

E 問題では、その中心から距離 `diameter // 2` にある元の頂点を、中心から出る枝ごとに集計する。異なる枝にある同色の頂点同士を組み合わせる。全体を線形時間に保つには、枝ごとの探索で毎回長さ `N` の距離配列を作らず、共有の訪問配列や `(頂点, 親, 距離)` を使って全枝を合計 `O(N)` で巡回する。

## References

- [ABC482 E - Diameter Endpoint Colors](https://atcoder.jp/contests/abc482/tasks/abc482_e): 同色の直径端点の組を数える問題の条件を確認した。
- [自分の解答](../../src/abc482/e.py): BFS 2回、親配列による経路復元、辺への補助頂点の挿入を参考にした。

## Related

- 問題: [ABC482 E - Diameter Endpoint Colors](https://atcoder.jp/contests/abc482/tasks/abc482_e)
- 自分の解答: [../../src/abc482/e.py](../../src/abc482/e.py)
- [重心](./tree_centroids.md)、[BFS](./bfs.md)
