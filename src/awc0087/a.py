T, X, Y = map(int, input().split())
A = input()
B = input()

ans = 0
d = {"L": -1, "R": 1, "S": 0}
for i in range(T):
    X += d[A[i]]
    Y += d[B[i]]
    if X == Y:
        ans += 1

print(ans)
