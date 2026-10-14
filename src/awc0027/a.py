N, S, T = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for a in A:
    if abs(a - S) <= T:
        ans += 1

print(ans)
