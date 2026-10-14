# mod_comb

## Summary

| やりたいこと | 使うもの |
| --- | --- |
| mod なし、または任意 mod で1個だけ | `math.comb` |
| 素数 mod で `k` が小さい | `comb_small_k` |
| 素数でない mod で、同じ `n` の二項係数をまとめて求める | `pascal_row` |
| 素数 mod で二項係数を何度も求める | `ModComb` |

`comb_small_k` と `ModComb` は素数 mod 用。
`pascal_row` は合成数 mod でも使える。

## Functions

### k が小さい二項係数を1回求める

`comb_small_k(n, k, mod)`

- 素数 `mod`、`min(k, n-k) < mod` が必要
- `nCk mod mod` を返す
- `O(min(k, n-k) + log mod)`、メモリ `O(1)`

### 合成数 mod で同じ n の二項係数をまとめて求める

`pascal_row(n, mod)`

- `[nC0, nC1, ..., nCn] mod mod` を返す
- 任意の正の `mod` で使える
- 時間 `O(n^2)`、メモリ `O(n)`

### 素数 mod で二項係数を何度も求める

`ModComb(max_n, mod)`

- 素数 `mod`、`max_n < mod` が必要
- 前計算は時間・メモリともに `O(max_n)`
- `mc.comb(n, k)`: `nCk mod mod` を `O(1)` で返す
- `mc.perm(n, k)`: `nPk mod mod` を `O(1)` で返す

`k < 0` または `k > n` の二項係数は `0`。
上の条件を満たさない大きな入力には Lucas の定理や CRT などが必要。

## Usage

```python
from math import comb

from library.math.mod_comb import ModComb, comb_small_k, pascal_row

MOD = 10**9 + 7

# 1個だけ。k が小さい
ans = comb_small_k(10**18, 3, MOD)

# 合成数 mod でも 5C0 ... 5C5 を作れる
row = pascal_row(5, 12)
# [1, 5, 10, 10, 5, 1]

# 何度も求める
mc = ModComb(200000, MOD)
a = mc.comb(100, 20)
b = mc.perm(100, 20)

# mod なし、または任意 mod で1個だけ
c = comb(100, 20)
d = comb(100, 20) % 12
```

## References

- [CP-Algorithms - Binomial Coefficients](https://cp-algorithms.com/combinatorics/binomial-coefficients.html): 各計算法と適用条件
- [和から株式会社 - 二項定理とパスカルの三角形の関係](https://wakara.co.jp/mathlog/20211111): Pascal の漸化式
- [SciPy documentation - `scipy.linalg.pascal`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.pascal.html): 二項係数を並べた構造の命名
- [Python documentation - `math.comb`](https://docs.python.org/3/library/math.html#math.comb): Python 標準の二項係数

## Related

- [EDPC Y - Grid 2](https://atcoder.jp/contests/dp/tasks/dp_y) / [自分の解答](../../src/edpc/Y.py)
- [ABC160 F - Distributing Integers](https://atcoder.jp/contests/abc160/tasks/abc160_f) / [自分の解答](../../src/rerooting-dp/abc160-f.py)
- [Typical90 065 - RGB Balls 2](https://atcoder.jp/contests/typical90/tasks/typical90_bm) / [自分の解答](../../src/競プロ典型90問/065.py)
