N, P, T, C = map(int, input().split())

if N > 1:
    S = list(map(int, input().split()))
else:
    S = [-1]
S.sort()

if P >= T:
    print(0)
elif S[-1] >= T:
    print(C)
else:
    print(-1)
