N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

for a in A:
    if 0 <= a <= M:
        pass
    else:
        ans += min(abs(a - 0), abs(a - M))

print(ans)
