L, R = map(int, input().split())
N = int(input())

for i in range(N):
    l, r = map(int, input().split())
    L = max(L, l)
    R = min(R, r)
    print(max(0, R - L + 1))
