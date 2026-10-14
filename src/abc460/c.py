from heapq import heapify, heappop


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
heapify(A)
heapify(B)
ans = 0

while len(A) and len(B):
    if B[0] <= A[0] * 2:
        heappop(A)
        heappop(B)
        ans += 1
    else:
        heappop(A)

print(ans)
