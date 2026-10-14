N, M, Q = map(int, input().split())
PC = [input().split() for i in range(M)]

for _ in range(Q):
    T = input()
    ans = True
    for i in range(M):
        p, c = int(PC[i][0]), PC[i][1]
        if T[p - 1] != c:
            ans = False
    print("Yes" if ans else "No")
