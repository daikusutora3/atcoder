N, T = map(int, input().split())
AB = [list(map(int, input().split()))for i in range(N)]

ans = 0
for i in range(N):
    a, b = AB[i]
    ans += max(a - b*T, 0)

print(ans)