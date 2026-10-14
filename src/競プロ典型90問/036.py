N, Q = map(int, input().split())

xy = [list(map(int, input().split())) for i in range(N)]

xy.sort()
print(xy)
