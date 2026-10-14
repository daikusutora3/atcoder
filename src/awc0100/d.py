N = int(input())

A = list(map(int, input().split()))
ruiA = [0 for i in range(N + 1)]

for i in range(N):
    ruiA[i + 1] += ruiA[i] + A[i]


s = sum(A)
ans = float("inf")
for k in range(1, N):
    ans = min(ans, abs(ruiA[k] - (s - ruiA[k])))

print(ans)
