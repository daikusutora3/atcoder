# 15 14
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 3 7
# 4 8
# 4 9
# 5 10
# 5 11
# 6 12
# 6 13
# 7 14
# 7 15


N, M = map(int, input().split())
tree = [[] for i in range(N)]
res = []
for _ in range(N - 1):
    u, v = map(int, input().split())
    res.append(u)

print(*res)
