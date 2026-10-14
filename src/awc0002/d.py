from sortedcontainers import SortedList


N,M = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

C.sort()
R.sort()
C = SortedList(C)

for i in range(M):
    bl = C.bisect_right(R[i])
    if 0 < bl <= len(C):
        C.discard(C[bl-1])

print(N - len(C))
