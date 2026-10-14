N = int(input())
A = list(map(int, input().split()))
r = 1
ans = 0
for i in range(N):
    if i < r:
        ans += 1
        r = max(r, i + A[i])

print(ans)
