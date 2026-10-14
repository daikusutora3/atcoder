# compress

## Summary

- 重複ありの値列を、大小関係を保った `0, 1, ..., K - 1` に圧縮する
- 入力値はソート可能で、辞書のキーにできる型を想定する

## Functions

| Function | Input | Output | Complexity |
| --- | --- | --- | --- |
| `compress(values)` | `values: iterable[hashable]` | `(comp, vals, idx)` | `O(N log N)` |

- `values`: 入力列。重複があってよい。
- `comp`: `values` と同じ長さの圧縮後リスト。
- `vals`: 入力に登場した値を昇順に重複除去したリスト。
- `idx`: 元の値から圧縮後 index への辞書。
- `N` は `values` の長さ。

## Usage

### 基本

```python
from library.misc.compress import compress

a = [100, 10, 100, 50]
comp, vals, idx = compress(a)

print(comp)  # [2, 0, 2, 1]
print(vals)  # [10, 50, 100]
print(idx[50])  # 1
```

`src/awc0061/e.py` のように、圧縮済み index と元値リストを使う場合は次のように書ける。

```python
from library.misc.compress import compress

h = [8, 3, 10, 5]
comp, vals, idx = compress(h)

print(comp)  # [2, 0, 3, 1]
print(vals)  # [3, 5, 8, 10]
print(idx[10])  # 3
```

## References

- [CP-Algorithms Library - compress_coords.hpp](https://lib.cp-algorithms.com/cp-algo/util/compress_coords.hpp.html)
  - ソート後に重複をまとめ、元の値の昇順配列を返す構成を参考にした
- [座標圧縮 - yaketake08's 実装メモ](https://tjkendev.github.io/procon-library/cpp/geometry/compress.html)
  - `O(N log N)` で値を昇順の連番へ対応させる基本方針を確認した

## Related

- 問題: [AtCoder Weekday Contest 0061 E](https://atcoder.jp/contests/awc0061/tasks/awc0061_e)
- 自分の解答: [../../src/awc0061/e.py](../../src/awc0061/e.py)
