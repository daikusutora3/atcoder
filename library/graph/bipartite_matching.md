# bipartite_matching

## Summary

- 二部グラフの最大マッチングを非再帰 Hopcroft–Karp 法で求める。
- `BipartiteMatching(n, m)` に `add_edge(u, v)` で辺を追加して使う。左右それぞれ 0-indexed。
- `solve()` は最大マッチング数、`pairs()` は対応する `(左, 右)` のリストを返す。
- 左頂点数を `n`、右頂点数を `m` とし、`0 <= u < n`、`0 <= v < m`。空のグラフ・孤立点・重複辺を扱える。
- 容量 1 の `始点 → 左 → 右 → 終点` の最大流に対応する。始点・終点・逆辺オブジェクトを省略して定数倍を減らす。一般の容量を扱う場合は [max_flow](./max_flow.md) を使う。
- 入力の隣接リストは変更しない。再帰や外部ライブラリは使用しない。

## Functions

| API | 内容・返り値 | 計算量 |
| --- | --- | --- |
| `BipartiteMatching(n, m)` | 左 `n` 頂点、右 `m` 頂点で作成 | `O(n)` |
| `add_edge(u, v)` | 左 `u` と右 `v` を結ぶ辺を追加 | ならし `O(1)` |
| `solve()` | 最大マッチング数を返す | `O((V + E)√V)`、変更がなければ `O(1)` |
| `pairs()` | マッチした `(u, v)` のリストを左頂点順で返す | 計算済みなら `O(n)`、未計算なら先に `solve()` |
| `bipartite_matching(adj, m)` | 従来の関数 API。左頂点ごとの相手を返し、未対応は `-1` | `O((V + E)√V)` |

`V = n + m`、`E` は追加した辺数。記憶領域は `O(V + E)`。
`solve()` は追加分ではなく、その時点の最大マッチング数を返す。
計算後に辺を追加した場合、次の `solve()` / `pairs()` で最初から再計算する。
辺をまとめて追加してから呼ぶと効率がよい。
`pairs()` の返り値を変更しても内部状態には影響しない。
同じ頂点への重複辺はマッチング数を増やさない。

## Usage

```python
from library.graph.bipartite_matching import BipartiteMatching

graph = BipartiteMatching(2, 2)
graph.add_edge(0, 0)
graph.add_edge(0, 1)
graph.add_edge(1, 0)

flow = graph.solve()
print(flow)  # 2
for i, j in graph.pairs():
    print(i, j)  # 0 1 / 1 0
```

左側をすべてマッチさせられるかは `graph.solve() == n` で判定する。
左右両方の全頂点を覆う完全マッチングの条件は `n == m == graph.solve()`。

すでに隣接リストがある場合は、従来の関数もそのまま使える。

```python
from library.graph.bipartite_matching import bipartite_matching

match = bipartite_matching([[0, 1], [0]], 2)
print(match)  # [1, 0]
```

提出時は `bipartite_matching.py` 全体を解答の先頭に貼り付ける。
クラスを使わない場合は関数だけの貼り付けでもよい。

典型90の077では、元の解答の変数名・方向辞書・辺追加・方向復元の流れを保ち、
`MFGraph` を `BipartiteMatching` に置き換えている。
始点・終点は不要で、`add_edge(i, j)` → `solve()` → `pairs()` の順に使う。
各 A 座標から8方向の移動先を辞書で調べるため、`E <= 8N`。
全体の計算量は `O(N√N)`、記憶領域は `O(N)`。

## Validation

リポジトリのルートで `.pypy/bin/python scripts/test_max_flow.py` を実行する。

- 小規模の二部グラフ1,500件で、クラス版・関数版を部分集合 DP と照合する。
- 再呼び出し、計算後の辺追加、`solve()` 前の `pairs()`、空グラフも確認する。
- 長さ5万の交互路で非再帰の増加路探索と復元を確認する。
- 解答の公式サンプル3件、ランダム500件、Hall条件による不可能例、大きい座標を確認する。
- 汎用最大流も、小規模2,000件で全カット列挙との一致、容量制約、流量保存などを確認する。

最大サイズ `N = 20000` の格子を全8方向にずらし、入力順をシャッフルした24ケース
（200×100、10000×2、1000×20）では、手元の PyPy 7.3.20 / Python 3.11 で
最も遅いケースが約0.50秒だった。起動・入力・出力を含み、到着座標も検証した。
AtCoder の実行環境での測定・提出による AC 確認はしていない。

## References

- [AC Library MaxFlow](https://atcoder.github.io/ac-library/master/document_ja/maxflow.html)
  - 元の解答に近い「グラフを作る → 辺を追加 → 個数を求める → 対応を復元する」使用感を参考にした。

- [SciPy: maximum_bipartite_matching](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.maximum_bipartite_matching.html)
  - Hopcroft–Karp 法の計算量と、未対応の相手を `-1` で表す API を確認した。SciPy への依存はない。
- [Dinic's algorithm - cp-algorithms](https://cp-algorithms.com/graph/dinic.html)
  - 単位ネットワークとしての二部マッチング、層ごとの増加路探索を参考にした。

## Related

- 問題: [競プロ典型90問 077 - Planes on a 2D Plane](https://atcoder.jp/contests/typical90/tasks/typical90_by)
- 自分の解答: [../../src/flow/typical90_by.py](../../src/flow/typical90_by.py)
- 関連問題: [AtCoder Library Practice Contest D - Maxflow](https://atcoder.jp/contests/practice2/tasks/practice2_d)
