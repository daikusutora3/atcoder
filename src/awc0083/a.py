N, D = map(int, input().split())

ans = 0
for _ in range(N):
    A, B = map(int, input().split())
    ans += A + B * D


print(ans)
