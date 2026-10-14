from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = True
for i in range(N):
    if B[A[i] - 1] != i + 1:
        ans = False


print("Yes" if ans else "No")
