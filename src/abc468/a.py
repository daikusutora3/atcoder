N = int(input())
ans = 0
A = list(map(int, input().split()))

for i in range(1, N - 1):
    if A[i - 1] < A[i] and A[i] > A[i + 1]:
        ans += 1

print(ans)
