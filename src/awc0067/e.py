N, K = map(int, input().split())
A = list(map(int, input().split()))

xor = 0
for i in range(N):
    xor ^= A[i] % (K + 1)

print("Aoki" if xor == 0 else "Takahashi")
