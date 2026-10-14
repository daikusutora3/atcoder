N = int(input())
A = list(map(int, input().split()))

ans = 0
max_a = A[0]
for i in range(N):
    if max_a < A[i]:
        max_a = A[i]
        ans = i

print(ans + 1 if ans != 0 else -1)
