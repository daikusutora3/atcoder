EPS = 1e-10


def sgn(x, eps=EPS):
    """x の符号を返す。eps 以内なら 0。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    if x > eps:
        return 1
    if x < -eps:
        return -1
    return 0


def add(a, b):
    """点・ベクトルの足し算。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    """点・ベクトルの引き算 a - b。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return (a[0] - b[0], a[1] - b[1])


def mul(a, k):
    """ベクトル a を k 倍する。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return (a[0] * k, a[1] * k)


def dot(a, b):
    """内積 a・b。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return a[0] * b[0] + a[1] * b[1]


def cross(a, b):
    """外積 a x b。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return a[0] * b[1] - a[1] * b[0]


def cross3(a, b, c):
    """(b - a) x (c - a) を返す。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return cross(sub(b, a), sub(c, a))


def norm2(a):
    """ベクトル a の長さの 2 乗。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return dot(a, a)


def dist2(a, b):
    """2 点 a, b の距離の 2 乗。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return norm2(sub(a, b))


def orientation(a, b, c):
    """a -> b -> c の向き。左折なら 1、右折なら -1、同一直線上なら 0。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return sgn(cross3(a, b, c))


def _between(x, l, r):
    """Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md"""
    return min(l, r) - EPS <= x <= max(l, r) + EPS


def on_segment(a, b, p):
    """点 p が線分 ab 上にあるか判定する。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return (
        sgn(cross3(a, b, p)) == 0
        and _between(p[0], a[0], b[0])
        and _between(p[1], a[1], b[1])
    )


def is_parallel(a, b, c, d):
    """直線 ab と直線 cd が平行か判定する。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return sgn(cross(sub(b, a), sub(d, c))) == 0


def is_orthogonal(a, b, c, d):
    """直線 ab と直線 cd が直交するか判定する。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    return sgn(dot(sub(b, a), sub(d, c))) == 0


def segments_intersect(a, b, c, d):
    """線分 ab と線分 cd が交差するか判定する。端点で接する場合も True。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    if o1 == 0 and on_segment(a, b, c):
        return True
    if o2 == 0 and on_segment(a, b, d):
        return True
    if o3 == 0 and on_segment(c, d, a):
        return True
    if o4 == 0 and on_segment(c, d, b):
        return True

    return o1 * o2 < 0 and o3 * o4 < 0


def line_intersection(a, b, c, d):
    """直線 ab と直線 cd の交点を返す。平行なら None。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    ab = sub(b, a)
    cd = sub(d, c)

    den = cross(ab, cd)
    if sgn(den) == 0:
        return None

    t = cross(sub(c, a), cd) / den
    return add(a, mul(ab, t))


def polygon_area2(poly):
    """多角形の符号付き面積の 2 倍を返す。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    n = len(poly)
    res = 0

    for i in range(n):
        res += cross(poly[i], poly[(i + 1) % n])

    return res


def convex_hull(points):
    """Andrew's monotone chain で凸包を反時計回り順に返す。辺上の余分な点は含めない。

    Docs: https://github.com/daikusutora3/atcoder/blob/main/library/geometry/geometry.md
    """
    points = sorted(set(points))

    if len(points) <= 1:
        return points

    lower = []
    for p in points:
        while len(lower) >= 2 and sgn(cross3(lower[-2], lower[-1], p)) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and sgn(cross3(upper[-2], upper[-1], p)) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]
