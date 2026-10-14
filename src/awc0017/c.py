N, Q = map(int, input().split())
C = list(map(int, input().split()))

A = [0 for i in range(N)]
for i in range(N - 1):
    A[i + 1] += A[i] + (1 if C[i] == C[i + 1] else 0)

for _ in range(Q):
    l, r = map(int, input().split())
    print(A[r - 1] - A[l - 1])
