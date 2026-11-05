# tree_centroids

## Summary

- 無向木の重心をすべて求める。結果は1頂点、または隣り合う2頂点。
- 重心は、その頂点を取り除いた後の各連結成分の頂点数が、元の頂点数 `N` の半分以下になる頂点。除去後の最大連結成分の頂点数を最小にする頂点でもある。
- 入力は 0-indexed の隣接リスト。空でない連結な単純無向木を渡し、各辺を両方向に登録する。入力の検査は行わない。
- 非再帰で根付き木の順序を作り、逆順に部分木サイズを集計する。深い木でも再帰上限の変更は不要。
- 距離で定義する木の「中心」とは別の概念。ABC482 E で直径を扱う際に必要なのは中心であり、重心へ置き換えることはできない。

## Functions

| Function | Output | Complexity |
| --- | --- | --- |
| `tree_centroids(graph)` | 重心の頂点配列 `list[int]`。順序は未規定 | 時間 `O(N)`、追加空間 `O(N)` |

`N` は頂点数。各頂点について、子側の各部分木サイズと、親側の `N - size[v]` の最大値を確認する。1頂点の木では `[0]` を返す。単独で貼り付けて使える。

## Usage

```python
from library.graph.tree_centroids import tree_centroids
from library.graph.tree_diameter import tree_centers

assert tree_centroids([[]]) == [0]
assert set(tree_centroids([[1], [0]])) == {0, 1}

# 0 に葉4個と、長さ3の枝がついた木。
graph = [[1, 2, 3, 4, 5], [0], [0], [0], [0], [0, 6], [5, 7], [6]]
assert tree_centroids(graph) == [0]
assert tree_centers(graph) == [5]  # 中心と重心は一致するとは限らない。
```

## References

- 今回は既存の外部実装を参照せず、部分木サイズに基づく重心の定義から実装した。

## Related

- 関連する用途: 重心分解の重心選択。重心分解全体は実装していない。
- 対応する自分の解答は未確認。
- [木の直径・中心](./tree_diameter.md)
