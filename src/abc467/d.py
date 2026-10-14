def solve():
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    A1 = 2 * (x2 - x1)
    B1 = 2 * (y2 - y1)
    C1 = x1**2 - x2**2 + y1**2 - y2**2
    A2 = 2 * (x4 - x3)
    B2 = 2 * (y4 - y3)
    C2 = x3**2 - x4**2 + y3**2 - y4**2
    if B1 * A2 == A1 * B2 and C2 * A1 != C1 * A2:
        print("No")
    elif B1 * A2 == A1 * B2 and C2 * B1 != C1 * B2:
        print("No")
    else:
        print("Yes")


T = int(input())

for _ in range(T):
    solve()
