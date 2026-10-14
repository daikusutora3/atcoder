# binary_search

## Summary

- 単調な判定関数 `is_ok(x)` について、`True` になる最大の整数 `x` を探すコピペ用スニペット
- 先に `is_ok(x)` を定義してから使う
- `ok = 0` が `True`、どこかで `False` になることを前提に、`ng` を倍々で広げてから二分探索する

## Snippet

```python
ok = 0
ng = 1

while is_ok(ng):
    ok = ng
    **ng** *= 2

while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

ans = ok
```

- `ans`: `is_ok(x)` が `True` になる最大の `x`
- 計算量: `O(log ans)` 回の判定

## Usage

```python
def is_ok(x):
    return x * x <= 50


ok = 0
ng = 1

while is_ok(ng):
    ok = ng
    ng *= 2

while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

ans = ok
print(ans)  # 7
```

## References

- [Binary Search - Algorithms for Competitive Programming](https://cp-algorithms.com/num_methods/binary_search.html)
  - 単調述語で境界を探す考え方と、境界不変条件を参考にした
- [bisect - Array bisection algorithm - Python documentation](https://docs.python.org/3/library/bisect.html)
  - 二分探索が挿入点、つまり境界を返す API として使われる点を確認した

## Related

- 問題: [AtCoder Beginner Contest 457 D](https://atcoder.jp/contests/abc457/tasks/abc457_d)
- 自分の解答: [../../src/abc457/d.py](../../src/abc457/d.py)
