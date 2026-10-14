N = int(input())
A = list(map(int, input().split()))
now = 1
ans = 1
for i in range(N - 1):
    if A[i] < A[i + 1]:
        now += 1
        ans = max(ans, now)
    else:
        now = 1

print(ans)
