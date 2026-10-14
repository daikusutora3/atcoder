# divisor_transform

## Summary

- 正整数の約数・倍数関係に対するゼータ変換とメビウス変換
- 配列は `1-indexed` 前提で、`a[0]` は使わない
- すべて in-place に `a` を書き換える
- 約数・倍数を直接なめる単純版。計算量の本質は `N/1 + N/2 + ... + N/N = O(N log N)` になること

## Idea

倍数系は「`k` の倍数にある値を全部集める」変換。

```text
G[k] = f[k] + f[2k] + f[3k] + ...
```

例えば頻度列 `cnt[x]` に倍数ゼータ変換をすると、`cnt[k]` は「入力にある `k` の倍数の個数」になる。これが倍数系ゼータ変換が便利になる一番よくある場面。

ABC162 E では `1..K` の中の `k` の倍数の個数が `K // k` で直接分かるので、倍数ゼータ変換は不要だった。入力配列の頻度から倍数個数を作る問題なら、ここで倍数ゼータ変換を使う。

倍数メビウス変換は、`G[k]` から `f[k]` に戻す処理。

```text
f[k] = G[k] - f[2k] - f[3k] - f[4k] - ...
```

`k` を大きい方から見ると、右辺の `f[2k], f[3k], ...` はすでに復元済み。だから降順に引いていけばよい。

約数系は向きが逆。

```text
G[n] = f[1] + ... + f[d] + ... + f[n]  (d divides n)
```

なので、

```text
f[n] = G[n] - sum of f[d] for d divides n and d < n
```

こちらは小さい約数から復元するので、昇順に見る。

どの変換も `k, 2k, 3k, ...` のように倍数をなめる。全体のループ回数は

```text
floor(N/1) + floor(N/2) + ... + floor(N/N) = O(N log N)
```

ここで調和級数が出る。

## Snippet

### 倍数ゼータ変換

`a[k]` を `a[k] + a[2k] + a[3k] + ...` に変える。`a[0]` は使わない。

```python
M = len(a) - 1
f = a[:]
for k in range(1, M + 1):
    a[k] = 0

for k in range(1, M + 1):
    for x in range(k, M + 1, k):
        a[k] += f[x]
```

- 変換後: `a[k] = sum of f[x] where k divides x`
- 計算量: `O(M log M)`

### 倍数メビウス変換

`G[k] = f[k] + f[2k] + f[3k] + ...` から `f[k]` に戻す。`a` に `G` が入っている前提。

```python
M = len(a) - 1
for k in range(M, 0, -1):
    for x in range(k * 2, M + 1, k):
        a[k] -= a[x]
```

- 変換後: `a[k] = f[k]`
- 計算量: `O(M log M)`
- `mod` を取る場合は、内側で `a[k] %= mod` するか、最後に必要な値へ `% mod` する

### 約数ゼータ変換

`a[n]` を `n` の約数にある値の合計に変える。`a[0]` は使わない。

```python
M = len(a) - 1
f = a[:]
for n in range(1, M + 1):
    a[n] = 0

for d in range(1, M + 1):
    for n in range(d, M + 1, d):
        a[n] += f[d]
```

- 変換後: `a[n] = sum of f[d] where d divides n`
- 計算量: `O(M log M)`

### 約数メビウス変換

`G[n] = sum of f[d] where d divides n` から `f[n]` に戻す。`a` に `G` が入っている前提。

```python
M = len(a) - 1
for d in range(1, M + 1):
    for n in range(d * 2, M + 1, d):
        a[n] -= a[d]
```

- 変換後: `a[n] = f[n]`
- 計算量: `O(M log M)`

## Usage

### 倍数ゼータ・メビウス

```python
orig = [0, 10, 20, 30, 40, 50, 60]
a = orig[:]

M = len(a) - 1
f = a[:]
for k in range(1, M + 1):
    a[k] = 0

for k in range(1, M + 1):
    for x in range(k, M + 1, k):
        a[k] += f[x]

print(a[1:])  # [210, 120, 90, 40, 50, 60]

for k in range(M, 0, -1):
    for x in range(k * 2, M + 1, k):
        a[k] -= a[x]

print(a[1:])  # [10, 20, 30, 40, 50, 60]
```

### ABC162 E の形

```python
MOD = 10**9 + 7
N, K = map(int, input().split())

cnt = [0] * (K + 1)
for g in range(1, K + 1):
    cnt[g] = pow(K // g, N, MOD)

for g in range(K, 0, -1):
    for x in range(g * 2, K + 1, g):
        cnt[g] -= cnt[x]
    cnt[g] %= MOD

ans = 0
for g in range(1, K + 1):
    ans += g * cnt[g]
    ans %= MOD
print(ans)
```

## References

- [Multiple/Divisor Fast Zeta/Möbius Transform - sotanishy’s competitive programming library](https://sotanishy.github.io/cp-library-cpp/convolution/divisor_zeta_moebius_transform.hpp.html)
  - 約数方向・倍数方向の定義と、GCD/LCM 畳み込みとの対応を確認した
- [ゼータ・メビウス変換（部分集合関係） - AtCoderInfo](https://info.atcoder.jp/entry/algorithm_lectures/subset_zeta_mobius)
  - ゼータ変換とメビウス変換が互いに逆変換であること、加算を減算で戻す実装方針を確認した
- [ABC162 参加感想 - maspyのHP](https://maspypy.com/atcoder-%E5%8F%82%E5%8A%A0%E6%84%B3-2020-04-12abc-162)
  - ABC162 E で `B(d) = sum_{d|n} A(n)` の倍数ゼータ変換として見る整理を確認した

## Related

- 問題: [AtCoder Beginner Contest 162 E - Sum of gcd of Tuples (Hard)](https://atcoder.jp/contests/abc162/tasks/abc162_e)
- 自分の解答: [../../src/Inclusion-Exclusion-Principle/abc162_e.py](../../src/Inclusion-Exclusion-Principle/abc162_e.py)
