N = int(input())
A = list(map(int, input().split()))

ans = 0

for i in range(N):
    ans += abs(i + 1 - A[i])

print(ans // 2)
