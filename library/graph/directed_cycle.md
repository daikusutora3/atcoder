# directed_cycle

## Summary

- 有向グラフにサイクルが存在するかを判定するライブラリ
- サイクルの有無だけを見る関数と、サイクルを 1 つ復元する関数を持つ
- 入力は `graph[v]` に遷移先を持つ 0-indexed の隣接リストを想定する
- 多重辺と自己ループもそのまま扱える
- `starts` を指定すると、その開始頂点たちから到達できる範囲だけを見る
- Python では深い再帰が不安定になりやすいため、実装は反復 DFS にしている

## Functions

| Function | Input | Output | Complexity |
| --- | --- | --- | --- |
| `has_directed_cycle(graph, starts=None)` | `graph: list[list[int]]`, `starts: iterable[int] \| None` | `bool` | `O(V + E)` |
| `find_directed_cycle(graph, starts=None)` | `graph: list[list[int]]`, `starts: iterable[int] \| None` | `list[int]` | `O(V + E)` |

## Usage

### `has_directed_cycle`

```python
from library.graph.directed_cycle import has_directed_cycle

graph = [
    [1],
    [2],
    [0],
    [],
]

print(has_directed_cycle(graph))  # True

starts = [0, 3]
print(has_directed_cycle(graph, starts))  # True
```

### `find_directed_cycle`

```python
from library.graph.directed_cycle import find_directed_cycle

graph = [
    [1],
    [2],
    [0],
    [],
]

cycle = find_directed_cycle(graph)
print(cycle)  # 例: [0, 1, 2, 0]
```

## References

- [Checking a graph for acyclicity and finding a cycle in O(M) - cp-algorithms](https://cp-algorithms.com/graph/finding-cycle.html)
  - DFS の 3 状態管理と、親配列からサイクルを復元する方針を参考にした
- [sys.setrecursionlimit - Python 3.11 documentation](https://docs.python.org/3.11/library/sys.html#sys.setrecursionlimit)
  - 深い再帰はクラッシュ要因になりうるため、Python 実装では反復 DFS を優先した
- [AC Library Document - SCC](https://atcoder.github.io/ac-library/production/document_ja/scc.html)
  - 有向グラフ系ライブラリとして、入力前提と計算量を明示する書き方の参考にした

## Related

- 問題: [AtCoder Beginner Contest 456 E](https://atcoder.jp/contests/abc456/tasks/abc456_e)
- 自分の解答: [../../src/abc456/e.py](../../src/abc456/e.py)
