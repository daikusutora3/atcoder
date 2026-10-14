K, M = map(int, input().split())
A = set(map(int, input().split()))

B = list(map(int, input().split()))

ans = 0
for b in B:
    if b in A:
        ans += 1


print(ans)
