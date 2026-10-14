# CumulativeSum2D

## Summary

- 整数の長方形配列を前処理し、任意の長方形領域の和を定数時間で求める。
- 座標は 0-indexed、区間は半開区間。負の値も扱える。
- 入力配列は変更しない。構築後に入力を更新した場合は再構築する。

## Functions

| Function | Input | Output | Complexity |
| --- | --- | --- | --- |
| `CumulativeSum2D(a)` | `H × W` の整数配列 | 累積和を保持するインスタンス | 時間・空間 `O((H + 1)(W + 1))` |
| `cs.sum(x1, y1, x2, y2)` | 左上・右下の境界 | 領域内の和 | 時間・追加空間 `O(1)` |

- `cs.s[i][j]` は `a` の `[0, i) × [0, j)` の和。先頭行・列を 0 にして境界の分岐をなくす。
- クエリは `[y1, y2) × [x1, x2)`。引数は左上の `(x1, y1)`、右下の `(x2, y2)` の順。
- `0 <= y1 <= y2 <= H`、`0 <= x1 <= x2 <= W` が必要。不正な境界は `ValueError`。
- 空の領域の和は 0。空配列や幅 0 の配列も扱える。行の長さが異なる入力は `ValueError`。
- `y` は行、`x` は列。累積和はインスタンスが保持するので、クエリごとに渡す必要はない。
- `H, W >= 1` なら構築は時間・空間ともに `O(HW)`。Python では行への参照と行内の累積値を使い、内側ループの添字アクセスを減らしている。計算量は整数の加減算を定数時間としたもの。

## Usage

提出時はクラスを解答へコピーする。

```python
from library.misc.prefix_sum_2d import CumulativeSum2D

a = [
    [1, 2, 3],
    [4, 5, 6],
]
cs = CumulativeSum2D(a)
print(cs.sum(0, 0, 3, 2))  # 21: 全体
print(cs.sum(1, 0, 3, 2))  # 16: 右側の 2 列
print(cs.sum(2, 1, 3, 2))  # 6: 1 マス
print(cs.sum(0, 1, 3, 1))  # 0: 空の領域
```

1-indexed の閉区間で左上 `(r1, c1)`、右下 `(r2, c2)` が与えられる場合は、`cs.sum(c1 - 1, r1 - 1, c2, r2)` とする。

## References

- [2次元累積和 - AtCoder Heuristic Contest Memo](https://jetbead.github.io/AtCoderHeuristicContestMemo/Library/summed_area_table.html)
  - 半開区間の長方形を 4 つの累積値で求める方法と計算量を参考にした。本実装の引数順は `(x1, y1, x2, y2)` とする。
- [ABC366 D 公式解説](https://atcoder.jp/contests/abc366/editorial/10643)
  - 多次元累積和の包除と、先頭に 0 の境界を置く実装を確認した。本ライブラリは 2 次元のみを扱う。

## Related

- 問題: [ABC461 D - Count Subgrid Sum = K](https://atcoder.jp/contests/abc461/tasks/abc461_d)
- 自分の解答: [../../src/abc461/dnew.py](../../src/abc461/dnew.py)
  - 解答中の `rui_get(i, j, h, w)` は `cs.sum(j, i, j + w, i + h)` に対応する。
