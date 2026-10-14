X, Y, L, R, A, B = map(int, input().split())

ans = 0
for time in range(A, B):
    if L <= time < R:
        ans += X
    else:
        ans += Y

print(ans)
