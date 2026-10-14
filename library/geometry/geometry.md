# geometry

## Summary

- 2 次元の点を `(x, y)` で表す、競プロ用の基本図形ライブラリ
- 整数座標なら外積・内積・面積 2 倍は誤差なしで扱える
- 実数座標では `EPS = 1e-10` を使って符号判定する
- 線分交差は端点で接する場合も交差とみなす
- `convex_hull` は重複点を除き、凸包上の余分な一直線上の点は含めない

## Functions

| Function | Input | Output | Complexity |
| --- | --- | --- | --- |
| `sgn(x, eps=EPS)` | 数値 `x` | `1`, `-1`, `0` | `O(1)` |
| `add(a, b)` | 点・ベクトル `a`, `b` | `a + b` | `O(1)` |
| `sub(a, b)` | 点・ベクトル `a`, `b` | `a - b` | `O(1)` |
| `mul(a, k)` | ベクトル `a`, 数値 `k` | `k * a` | `O(1)` |
| `dot(a, b)` | ベクトル `a`, `b` | 内積 | `O(1)` |
| `cross(a, b)` | ベクトル `a`, `b` | 外積 | `O(1)` |
| `cross3(a, b, c)` | 3 点 `a`, `b`, `c` | `(b - a) x (c - a)` | `O(1)` |
| `norm2(a)` | ベクトル `a` | 長さの 2 乗 | `O(1)` |
| `dist2(a, b)` | 2 点 `a`, `b` | 距離の 2 乗 | `O(1)` |
| `orientation(a, b, c)` | 3 点 `a`, `b`, `c` | 左折 `1`、右折 `-1`、一直線 `0` | `O(1)` |
| `on_segment(a, b, p)` | 線分 `ab`, 点 `p` | `p` が線分上なら `True` | `O(1)` |
| `is_parallel(a, b, c, d)` | 直線 `ab`, `cd` | 平行なら `True` | `O(1)` |
| `is_orthogonal(a, b, c, d)` | 直線 `ab`, `cd` | 直交なら `True` | `O(1)` |
| `segments_intersect(a, b, c, d)` | 線分 `ab`, `cd` | 交差するなら `True` | `O(1)` |
| `line_intersection(a, b, c, d)` | 直線 `ab`, `cd` | 交点、平行なら `None` | `O(1)` |
| `polygon_area2(poly)` | 頂点列 `poly` | 符号付き面積の 2 倍 | `O(N)` |
| `convex_hull(points)` | 点列 `points` | 凸包頂点の反時計回り列 | `O(N log N)` |

## Usage

### 向き・線分交差

```python
from library.geometry.geometry import cross3, segments_intersect

a = (0, 0)
b = (4, 0)
c = (2, -1)
d = (2, 1)

print(cross3(a, b, d))  # 4
print(segments_intersect(a, b, c, d))  # True
```

### 多角形の面積と凸包

```python
from library.geometry.geometry import convex_hull, polygon_area2

points = [(0, 0), (2, 0), (1, 0), (2, 2), (0, 2)]
hull = convex_hull(points)

print(hull)  # [(0, 0), (2, 0), (2, 2), (0, 2)]
print(abs(polygon_area2(hull)) / 2)  # 4.0
```

### 直線の交点

```python
from library.geometry.geometry import line_intersection

p = line_intersection((0, 0), (2, 2), (0, 2), (2, 0))
print(p)  # (1.0, 1.0)

print(line_intersection((0, 0), (1, 0), (0, 1), (1, 1)))  # None
```

## References

- [CP-Algorithms - Basic Geometry](https://cp-algorithms.com/geometry/basic-geometry.html)
  - 点をベクトルとして扱い、内積・外積・長さの 2 乗を基本 API にする方針を確認した
- [CP-Algorithms - Check if two segments intersect](https://cp-algorithms.com/geometry/check-segments-intersection.html)
  - 向き判定と線分上判定を組み合わせる線分交差の標準形を確認した
- [CP-Algorithms - Convex Hull construction](https://cp-algorithms.com/geometry/convex-hull.html)
  - Andrew's monotone chain が `O(N log N)` で、ソート後にスタックで凸包を作る点を参考にした

## Related

- 問題: [AtCoder Weekday Contest 0103 E](https://atcoder.jp/contests/awc0103/tasks/awc0103_e)
- 自分の解答: [../../src/awc0103/e.py](../../src/awc0103/e.py)
