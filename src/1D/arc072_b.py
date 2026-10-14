# import sys
# from functools import lru_cache

# sys.setrecursionlimit(10**6)


# @lru_cache(maxsize=None)
# def dfs(x, y):
#     if x <= 1 and y <= 1:
#         return False
#     res = False
#     for i in range(1, x // 2 + 1):
#         res |= not dfs(x - 2 * i, y + i)
#     for i in range(1, y // 2 + 1):
#         res |= not dfs(x + i, y - 2 * i)
#     return res


# res = [[0 for y in range(21)] for x in range(21)]
# for x in range(21):
#     for y in range(21):
#         res[x][y] = 1 if dfs(x, y) else 0

# for r in res:
#     print(*r)

X, Y = map(int, input().split())

if abs(X - Y) <= 1:
    print("Brown")
else:
    print("Alice")
