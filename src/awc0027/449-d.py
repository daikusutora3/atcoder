L, R, D, U = map(int, input().split())
ans = 0
MAX = 10**6 + 1


def is_in(x, y):
    global L, R, D, U
    return L <= x <= R and D <= y <= U


for i in range(1, MAX):
    # 左下
    if is_in(-2 * i, -2 * i):
        ans -= 1
    # 左上
    if is_in(-2 * i, 2 * i):
        ans -= 1
    # 右上
    if is_in(2 * i, 2 * i):
        ans -= 1
    # 右下
    if is_in(2 * i, -2 * i):
        ans -= 1
    # bottom
    if D <= -2 * i <= U:
        if L <= -2 * i and 2 * i <= R:
            ans += 4 * i + 1
        elif -2 * i <= L and R <= 2 * i:
            ans += R - L + 1
        elif -2 * i <= L <= 2 * i:
            ans += 2 * i - L + 1
        elif -2 * i <= R <= 2 * i:
            ans += R + 2 * i + 1
    # top
    if D <= 2 * i <= U:
        if L <= -2 * i and 2 * i <= R:
            ans += 4 * i + 1
        elif -2 * i <= L and R <= 2 * i:
            ans += R - L + 1
        elif -2 * i <= L <= 2 * i:
            ans += 2 * i - L + 1
        elif -2 * i <= R <= 2 * i:
            ans += R + 2 * i + 1
    # left
    if L <= -2 * i <= R:
        if D <= -2 * i and 2 * i <= U:
            ans += 4 * i + 1
        elif -2 * i <= D and U <= 2 * i:
            ans += U - D + 1
        elif -2 * i <= D <= 2 * i:
            ans += 2 * i - D + 1
        elif -2 * i <= U <= 2 * i:
            ans += U + 2 * i + 1
    # right
    if L <= 2 * i <= R:
        if D <= -2 * i and 2 * i <= U:
            ans += 4 * i + 1
        elif -2 * i <= D and U <= 2 * i:
            ans += U - D + 1
        elif -2 * i <= D <= 2 * i:
            ans += 2 * i - D + 1
        elif -2 * i <= U <= 2 * i:
            ans += U + 2 * i + 1


if is_in(0, 0):
    ans += 1

print(ans)
