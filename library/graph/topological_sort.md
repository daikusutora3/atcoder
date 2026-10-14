      # topological_sort

## Summary

- 有向グラフのトポロジカルソートを行うライブラリ
- 入力は `graph[v]` に遷移先を持つ 0-indexed の隣接リストを想定する
- 閉路がある場合、トポロジカル順序は存在しないので `[]` を返す
- 多重辺と自己ループもそのまま扱える
- 入次数 0 の頂点から処理する Kahn 法で実装している

## Functions

| Function | Input | Output | Complexity |
| --- | --- | --- | --- |
| `topological_sort(graph)` | `graph: list[list[int]]` | `list[int]` | `O(V + E)` |

## Usage

```python
from library.graph.topological_sort import topological_sort

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)

order = topological_sort(graph)

if not order:
    print("cycle")
else:
    print(*(v + 1 for v in order))
```

## References

- [Topological sorting - Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)
  - Kahn 法が入次数 0 の頂点を順に取り出し、処理済み辺を取り除く考え方であることを確認した
- [graphlib - Python documentation](https://docs.python.org/3/library/graphlib.html)
  - トポロジカル順序の定義と、閉路があると完全な順序が作れない点を確認した

## Related

- 問題: [AtCoder Beginner Contest 223 D - Restricted Permutation](https://atcoder.jp/contests/abc223/tasks/abc223_d)
- 関連する自分の解答: [../../src/abc456/e.py](../../src/abc456/e.py)
