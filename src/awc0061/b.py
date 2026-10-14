N = int(input())
S = list(map(int, input().split()))
C = list(map(int, input().split())) if N > 1 else []

now = S[0]
ans = now

for i in range(N - 1):
    now = now + S[i + 1] - C[i]
    ans = max(ans, now)

print(ans)
