N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = -1
max_a = -1

for i, a in enumerate(A):
    if a > max_a:
        max_a = a
        ans = i

print(ans + 1)
