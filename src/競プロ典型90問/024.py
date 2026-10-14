N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


for i in range(N):
    K -= abs(A[i] - B[i])

print("Yes" if K >= 0 and K % 2 == 0 else "No")
