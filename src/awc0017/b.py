N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for _ in range(M):
    b = B[_]
    if b - 2 >= 0:
        A[b - 2] += 1
    A[b - 1] += 1
    if b < N:
        A[b] += 1

print(*A)
