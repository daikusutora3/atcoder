from sortedcontainers import SortedList

N, Q = map(int, input().split())
S = list(map(int, input().split()))
sl = SortedList(S[:])


for _ in range(Q):
    T, V = map(int, input().split())
    sl.discard(S[T - 1])
    S[T - 1] = V
    sl.add(S[T - 1])
    A = sl[(len(sl) + 1) // 2 - 1]
    print(sl.bisect_left(A))
