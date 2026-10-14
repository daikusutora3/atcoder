N, X = map(int, input().split())
A = list(map(int, input().split()))
B = [A[i] for i in range(N)]

for i in range(1, N - 1):
    if A[i - 1] == A[i + 1] and A[i - 1] != A[i]:
        B[i] = 0

ans = X

for i in range(N):
    ans ^= B[i]

print(ans)
