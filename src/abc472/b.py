N = int(input())

ans = float("inf")

L = list(map(int, input().split()))

for i in range(N):
    left = 0
    for l in range(i):
        left += L[l]
    right = 0
    for r in range(i, N):
        right += L[r]
    ans = min(ans, abs(left - right))

print(ans)
