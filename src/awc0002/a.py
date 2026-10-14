N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = -1
for i, a in enumerate(A):
    if a == K:
        ans = i+1
        break

print(ans)
