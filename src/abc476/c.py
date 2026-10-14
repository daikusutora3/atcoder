from sortedcontainers import SortedList

N = int(input())
A = list(map(int, input().split()))
sl = SortedList([-a for a in A[:2]])

for i in range(2, N):
    sl.add(-A[i])
    print(-sl[2])
