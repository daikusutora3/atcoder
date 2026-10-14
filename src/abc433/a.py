X, Y, Z = map(int, input().split())

ans = "No"
for _ in range(1000):
    if X == Y * Z:
        ans = "Yes"
    X += 1
    Y += 1

print(ans)
