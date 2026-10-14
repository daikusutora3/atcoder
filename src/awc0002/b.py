N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = set(map(int, input().split()))

ans = [0, 0]
for i, a in enumerate(A):
    if a < K and i+1 in B:
        ans[0] += 1
        ans[1] += a

print(*ans)