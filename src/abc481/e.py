# https://zenn.dev/asamichiruko/articles/a267450d8842d2
from functools import cmp_to_key


def half(p):
    """点 p が上半平面 (y > 0 または +x 軸上) に属する場合は 0 を, さもなくば 1 を返す"""
    x, y = p
    if y > 0 or (y == 0 and x >= 0):
        return 0
    else:
        return 1


def cross(a, b):
    """原点から見たベクトル a, b の外積 (符号付き面積) の値を返す"""
    ax, ay = a
    bx, by = b
    return ax * by - ay * bx


def norm2(p):
    """点 p の原点からの距離の二乗を返す"""
    x, y = p
    return x * x + y * y


def angle_cmp(a, b):
    """点 a, b の偏角と距離に基づく比較関数"""
    ha = half(a)
    hb = half(b)
    if ha < hb:
        return -1
    elif ha > hb:
        return 1

    c = cross(a, b)
    if c > 0:
        return -1
    elif c < 0:
        return 1

    da = norm2(a)
    db = norm2(b)
    if da < db:
        return -1
    elif da > db:
        return 1

    return 0


def is_same_dir(a, b):
    """点 a, b が原点でなく, かつ原点を始点とする同一半直線上にある場合は True を, さもなくば False を返す"""
    if (a[0] == 0 and a[1] == 0) or (b[0] == 0 and b[1] == 0):
        return False
    return half(a) == half(b) and cross(a, b) == 0


def solve():
    ans = 0
    N = int(input())
    points = []
    for i in range(N):
        X, Y = map(int, input().split())
        points.append((X, Y))
        points.sort(key=cmp_to_key(angle_cmp))

    for i in range(N):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % N]
        ok1 = -1
        ng1 = N
        while ng1 - ok1 > 1:
            mid = (ok1 + ng1) // 2
            if angle_cmp((-x1, -y1), points[mid]) == 1:
                ok1 = mid
            else:
                ng1 = mid

        ok2 = -1
        ng2 = N
        while ng2 - ok2 > 1:
            mid = (ok2 + ng2) // 2
            if angle_cmp((-x2, -y2), points[mid]) == 1:
                ok2 = mid
            else:
                ng2 = mid
        base = 0
        if y1 >= 0:
            base = ok1 - i
        else:
            base = i - 1 - ok1

        ans = max(base, N - base)
        if ok1 - ok2 >= 0:
            base += ok1 - ok2
        else:
            base += ok1 - ok2 - 1
        ans = max(base, N - base)
    print(ans)


T = int(input())
for _ in range(T):
    solve()
