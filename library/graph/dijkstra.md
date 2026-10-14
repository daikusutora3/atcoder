# dijkstra

## Summary

- 非負重みグラフの単一始点最短距離を求めるライブラリ
- 入力は `graph[v]` に `(to, cost)` を持つ 0-indexed の隣接リストを想定する
- 有向グラフ、無向グラフ、多重辺、自己ループを扱える
- 負辺がある場合は使えない
- 到達できない頂点の距離は `inf` のまま残る

## Functions

| Function | Input | Output | Complexity |
| --- | --- | --- | --- |
| `dijkstra(s, graph, inf=float("inf"))` | `s: int`, `graph: list[list[tuple[int, int]]]`, `inf: int \| float` | `list[int \| float]` | `O((V + E) log E)` |

## Usage

```python
from library.graph.dijkstra import dijkstra

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = dijkstra(0, graph)
print(-1 if dist[N - 1] == float("inf") else dist[N - 1])
```

整数の十分大きい値を使いたい場合:

```python
INF = 10**30
dist = dijkstra(0, graph, INF)
```

## References

- [Dijkstra Algorithm - cp-algorithms](https://cp-algorithms.com/graph/dijkstra.html)
  - 非負重みが前提であることと、優先度付きキューで古い候補を捨てる実装方針を参考にした
- [heapq - Python documentation](https://docs.python.org/3/library/heapq.html)
  - Python の最小ヒープ API と、優先度付きキューとして使う方針を確認した

## Related

- 問題: [競プロ典型 90 問 013 - Passing](https://atcoder.jp/contests/typical90/tasks/typical90_m)
- 自分の解答: [../../src/競プロ典型90問/013.py](../../src/競プロ典型90問/013.py)
- 自分の解答: [../../src/awc0044/d.py](../../src/awc0044/d.py)
- 自分の解答: [../../src/awc0058/d.py](../../src/awc0058/d.py)
- 自分の解答: [../../src/awc0061/d.py](../../src/awc0061/d.py)
