N = int(input())
ans = 1
MOD = 10**9 + 7
for _ in range(N):
    A = list(map(int, input().split()))
    ans = (ans * (sum(A))) % MOD

print(ans)
