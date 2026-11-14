N, P = map(int, input().split())
A = list(map(int, input().split()))
ans = 1
for i in range(N):
    ans = (ans * (A[i])) % P

print(ans)
