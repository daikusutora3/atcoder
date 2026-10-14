from bisect import bisect_left


Q = int(input())
S = input()
T = input()

ind = []

for i in range(len(S) - len(T) + 1):
    flag = True
    for j in range(len(T)):
        if S[i + j] != T[j]:
            flag = False
            break
    if flag:
        ind.append(i)

for _ in range(Q):
    L, R = map(int, input().split())
    bl = bisect_left(ind, L - 1)
    if bl < len(ind) and ind[bl] + len(T) <= R:
        print("Yes")
    else:
        print("No")
