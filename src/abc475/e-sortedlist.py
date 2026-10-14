from sortedcontainers import SortedList

N, M, K = map(int, input().split())
T = input()
sl = SortedList()

X = [["0" for k in range(K)] for i in range(N)]
for i in range(N):
    S = input()
    for k in range(K):
        if S[k] == T[k]:
            X[i][k] = "0"
        else:
            X[i][k] = "1"
    sl.add("".join(X[i]))
sl.add("1" * K)
Q = int(input())
for _ in range(Q):
    i, j = map(int, input().split())
    i, j = i - 1, j - 1
    sl.remove("".join(X[i]))
    X[i][j] = "0" if X[i][j] == "1" else "1"
    sl.add("".join(X[i]))
    m = M
    if M < sl.bisect_right(sl[M - 1]):
        m = sl.bisect_left(sl[M - 1])
    if m > 0 and "".join(X[i]) <= sl[m - 1]:
        print("Yes")
    else:
        print("No")
