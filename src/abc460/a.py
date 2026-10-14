N, M = map(int, input().split())

ans = 0
while M != 0:
    M = N % M
    ans += 1

print(ans)
