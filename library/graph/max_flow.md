# max_flow

## Summary

- 非再帰 Dinic 法で有向グラフの最大流を求める。0-indexed、容量は非負整数。
- 多重辺、逆向きの辺、自己ループ、容量 0 に対応する。
- 辺の行き先と残余容量を平坦な配列に保存し、逆辺を `e ^ 1` で参照する。深い経路でも再帰制限に依存しない。
- `flow` は残余グラフを更新する。同じ始点・終点で再度呼ぶと、追加で流した量を返す。
- `MFGraph` は構築・流量計算・復元で状態を共有するためクラスとして提供する。ACL の完全な互換実装ではなく、`change_edge` は提供しない。

## Functions

`V` は頂点数、`E` は `add_edge` で追加した辺数。記憶領域は `O(V + E)`。

| API | 内容・返り値 | 計算量 |
| --- | --- | --- |
| `MFGraph(n)` | `n` 頂点のグラフを作る | `O(V)` |
| `add_edge(src, dst, cap)` | 辺を追加し、追加順の辺 ID を返す | ならし `O(1)` |
| `flow(s, t, flow_limit=None)` | 今回追加で流した量。`s != t`。上限を省略すると最大まで流す | 一般に `O(V²E)` |
| `edge_flow(i)` | 辺 ID `i` に現在流れている量 | `O(1)` |
| `get_edge(i)` | `Edge(src, dst, cap, flow)`。`cap` は元の容量 | `O(1)` |
| `edges()` | 追加順の `Edge` のリスト | `O(E)` |
| `min_cut(s)` | 残余グラフで `s` から到達可能な頂点の bool リスト | `O(V + E)` |

`min_cut(s)` が最小カットを表すのは、`s` から対象の終点へ最大まで流した後。
`flow_limit` によって途中で止めた場合は、最小カットとは限らない。
`g`, `to`, `cap` は内部状態なので直接書き換えない。

二部マッチングを `s → 左側 → 右側 → t` の容量 1 のネットワークにすると、
Dinic の計算量は `O((V + E)√V)`。典型90の077では `V = 2N + 2`、
`E ≤ 10N` なので全体で `O(N√N)`、記憶領域 `O(N)`。
一般の容量 1 のネットワークすべてに、この二部マッチング用の計算量が適用できるわけではない。

## Usage

提出時は `max_flow.py` の内容を解答に貼り付ける。ローカルで import する場合:

```python
from library.graph.max_flow import MFGraph

# 左 0, 1、右 2, 3、始点 4、終点 5
graph = MFGraph(6)
candidates = []
for u, v in [(0, 2), (0, 3), (1, 2)]:
    e = graph.add_edge(u, v, 1)
    candidates.append((e, u, v))
for u in (0, 1):
    graph.add_edge(4, u, 1)
for v in (2, 3):
    graph.add_edge(v, 5, 1)

print(graph.flow(4, 5))  # 2
for e, u, v in candidates:
    if graph.edge_flow(e):
        print(u, v)  # 0 3 / 1 2
```

復元に必要な辺 ID と付随情報（移動方向など）を構築時に保存しておくと、
`edges()` による全辺のオブジェクト生成や、方向の再計算を省ける。

## Validation

リポジトリのルートで `.pypy/bin/python scripts/test_max_flow.py` を実行する。
小規模のランダムグラフ2,000件を全カット列挙と照合し、容量制約・流量保存・
流量上限・継続呼び出し・5万頂点の経路を検証する。
解答は小規模500件で部分集合 DP と判定を比較し、復元した到着座標も検証する。

典型90の077は二部マッチングなので、提出コードでは、さらに定数倍を削減した
[bipartite_matching.py](./bipartite_matching.md) を使用する。
容量が一般の整数の場合や、二部グラフ以外の最大流にはこの `MFGraph` を使う。

## References

- [AC Library MaxFlow](https://atcoder.github.io/ac-library/master/document_ja/maxflow.html)
  - 辺 ID、流量上限、辺の復元、残余グラフの到達可能性という API の意味を参考にした。
- [Dinic's algorithm - cp-algorithms](https://cp-algorithms.com/graph/dinic.html)
  - 層グラフと current arc による探索、および二部マッチングの計算量を確認した。
- [ac-library-python の maxflow.py](https://github.com/not522/ac-library-python/blob/master/atcoder/maxflow.py)
  - 元コードの辺オブジェクト・逆辺参照・非再帰探索を確認し、平坦な配列とローカル変数で処理する方針を採った。

## Related

- 問題: [競プロ典型90問 077 - Planes on a 2D Plane](https://atcoder.jp/contests/typical90/tasks/typical90_by)
- 自分の解答（二部マッチング専用版を使用）: [../../src/flow/typical90_by.py](../../src/flow/typical90_by.py)
- 関連問題: [AtCoder Library Practice Contest D - Maxflow](https://atcoder.jp/contests/practice2/tasks/practice2_d)
