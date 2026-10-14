T = int(input())

for _ in range(T):
    X1, Y1, R1, X2, Y2, R2 = map(int, input().split())
    if R1 < R2:
        X1, Y1, R1, X2, Y2, R2 = X2, Y2, R2, X1, Y1, R1

    if (R1 - R2) ** 2 <= abs(X1 - X2) ** 2 + abs(Y1 - Y2) ** 2 <= (R1 + R2) ** 2:
        print("Yes")
    else:
        print("No")
