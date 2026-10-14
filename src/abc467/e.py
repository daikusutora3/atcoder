N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

plus = []

for i in range(N - 1):
    # (A[i] + A[i+1])% M  -> B[i]
    plus.append((B[i] - A[i] - A[i + 1]) % M)
    A[i + 1] += (B[i] - A[i] - A[i + 1]) % M

print(A)
print(plus)
