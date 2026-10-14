# prime_factor

## Summary

- 正整数 `n` を素因数分解し、`[(p, e), ...]` の形で返す
- `n == 1` の素因数分解は空リスト `[]`
- 返り値は素数 `p` の昇順
- 多数の値を分解するなら、最大値までの `spf` を先に作る方法が速い

### 方法ごとの使い分け

| Method | Good | Bad | Typical use |
| --- | --- | --- | --- |
| 素数リスト `sieve_primes` + `factorize_by_primes` | `sqrt(max n)` までの前処理で大きい値も扱える | 各分解で `sqrt(x)` までの素数を見る | `x` が大きい、または少数クエリ |
| SPF `build_spf` + `factorize_spf` | 実装が単純で、Python では速いことが多い | `O(max n)` メモリが必要 | `n <= 10^6..10^7` の多数クエリ |
| 線形篩 `build_linear_spf` | SPF と素数列を `O(max n)` で同時に作れる | `primes` も返すぶん保持データが増える | 素数列も同時に欲しい場合 |

このファイルでは AtCoder で貼りやすい素数リストによる試し割り・SPF・線形篩を実装する。

## Functions

| Function | Input | Output | Complexity |
| --- | --- | --- | --- |
| `sieve_primes(n)` | `n: int >= 0` | `n` 以下の素数リスト | `O(n log log n)` |
| `factorize_by_primes(n, primes)` | `n: int >= 1`, `primes` | `[(p, e), ...]` | `O(pi(sqrt(n)))` |
| `build_spf(n)` | `n: int >= 0` | `spf` | `O(n log log n)` |
| `build_linear_spf(n)` | `n: int >= 0` | `(spf, primes)` | `O(n)` |
| `factorize_spf(n, spf)` | `1 <= n < len(spf)` | `[(p, e), ...]` | `O(log n)` |
| `divisors_from_factorization(factors)` | `[(p, e), ...]` | 約数の昇順リスト | `O(d(n) log d(n))` |

- `spf[x]` は `x` の最小素因数。`spf[1] == 1`。
- `factorize_by_primes` は `sqrt(n)` までの素数が `primes` に含まれている前提。
- SPF だけ欲しいなら `build_spf` を使う。素数列も同時に欲しいなら `build_linear_spf` を使う。
- `d(n)` は `n` の約数個数。

## Usage

### 最大値が大きい場合は素数リストで割る

```python
from library.math.prime_factor import factorize_by_primes, sieve_primes

x = 99991 * 1000003
primes = sieve_primes(int(x**0.5) + 1)
# primes は 316223 以下の素数リスト

factors = factorize_by_primes(x, primes)
print(factors)  # [(99991, 1), (1000003, 1)]
# x = 99991 * 1000003

print(factorize_by_primes(1, primes))  # []
# 1 は素因数を持たないので空リスト
```

### 多数クエリなら SPF

```python
from library.math.prime_factor import build_spf, factorize_spf

a = [12, 36, 97]
spf = build_spf(max(a))
# spf[12] == 2, spf[36] == 2, spf[97] == 97

for x in a:
    print(factorize_spf(x, spf))
# [(2, 2), (3, 1)]  12 = 2^2 * 3
# [(2, 2), (3, 2)]  36 = 2^2 * 3^2
# [(97, 1)]         97 は素数
```

### 線形篩で SPF と素数列を同時に作る

```python
from library.math.prime_factor import build_linear_spf, factorize_spf

spf, primes = build_linear_spf(30)
# primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print(factorize_spf(24, spf))  # [(2, 3), (3, 1)]
# 24 = 2^3 * 3
```

### 約数列へ変換する

```python
from library.math.prime_factor import divisors_from_factorization

factors = [(2, 2), (3, 2)]
# 36 = 2^2 * 3^2

divs = divisors_from_factorization(factors)
print(divs)  # [1, 2, 3, 4, 6, 9, 12, 18, 36]
# 36 の正の約数を昇順で返す
```

## References

- [CP-Algorithms - Integer factorization](https://cp-algorithms.com/algebra/factorization.html)
  - 素数リストによる分解など、分解手法ごとの適用範囲を確認した
- [CP-Algorithms - Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html)
  - 素数列を前処理して分解に使う場合の計算量を確認した
- [CP-Algorithms - Linear Sieve](https://cp-algorithms.com/algebra/prime-sieve-linear.html)
  - 最小素因数 `lp` を線形時間で作る実装方針を参考にした

## Related

- 問題: [Typical Contest 90 030 - K Factors](https://atcoder.jp/contests/typical90/tasks/typical90_ad)
- 自分の解答: [../../src/競プロ典型90問/030.py](../../src/競プロ典型90問/030.py)
- 問題: [Typical Contest 90 075 - Magic For Balls](https://atcoder.jp/contests/typical90/tasks/typical90_bw)
- 自分の解答: [../../src/競プロ典型90問/075.py](../../src/競プロ典型90問/075.py)
