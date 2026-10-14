# T = int(input())


def solve():
    A, B, X, Y = map(int, input().split())
    if X < 0:
        X *= -1
    if Y < 0:
        Y *= -1
    if X == Y:
        print(min(2 * X * A, 2 * X * B))
        return
    if A > B:
        A, B = B, A
        X, Y = Y, X
    if X < Y:
        cost = 2 * X * A
        cost1 = (
            cost
            + 3 * A * ((Y - X) // 2 + (1 if (Y - X) % 2 else 0))
            + A * ((Y - X) // 2)
        )
        cost2 = (
            cost + B * ((Y - X) // 2 + (1 if (Y - X) % 2 else 0)) + A * ((Y - X) // 2)
        )
        print(min(cost1, cost2))
    else:
        cost = 2 * Y * A
        cost1 = (
            cost
            + 3 * A * ((X - Y) // 2)
            + A * ((X - Y) // 2 + (1 if (X - Y) % 2 else 0))
        )
        cost2 = (
            cost + B * ((X - Y) // 2) + A * (((X - Y) // 2) + (1 if (X - Y) % 2 else 0))
        )
        print(min(cost1, cost2))


T = int(input())
for _ in range(T):
    solve()
