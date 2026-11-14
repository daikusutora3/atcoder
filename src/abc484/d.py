from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)

ans = 0
for i in range(N):
    if i > 0 and A[i] == A[i - 1]:
        d[A[i]] += 1
        continue
    # print(i, d[A[i]], i - d[A[i]])
    ans += i - d[A[i]]
    d[A[i]] += 1

print(ans + 1)
