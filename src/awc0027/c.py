N = int(input())
X = list(map(int, input().split()))
X.sort()
ans = 0
for i in range(N - 1):
    ans = max(ans, abs(X[i + 1] - X[i]))

print(ans)
