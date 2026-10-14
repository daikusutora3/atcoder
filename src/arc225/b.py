# from functools import lru_cache
# from itertools import combinations


# win = set()


# def solve():
#     N = int(input())
#     A = list(input().split())

#     @lru_cache()
#     def dfs(bit: int):
#         global win
#         res = False
#         if bit == 0:
#             return res
#         for num in range(1, bit.bit_count() + 1):
#             for com in combinations(
#                 [i for i in range(bit.bit_length()) if bit >> i & 1], num
#             ):
#                 n_bit = bit
#                 is_ok = True
#                 for i in range(len(com) - 1):
#                     if com[i] + 1 == com[i + 1]:
#                         is_ok = False
#                 if not is_ok:
#                     continue
#                 for c in com:
#                     n_bit ^= 1 << c
#                 res |= not dfs(n_bit)
#         if not res:
#             win.add(bin(bit)[2:])
#         return res

#     print(dfs(int("".join(A), 2)))


# solve()
# print(win)

from atcoder.dsu import DSU

T = int(input())


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    dsu = DSU(N)

    for i in range(N - 1):
        if A[i] == A[i + 1] and A[i] == 1:
            dsu.merge(i, i + 1)

    ans = True
    for i in range(N):
        if A[i] == 1:
            if dsu.size(i) != 2:
                ans = False

    if ans:
        print("Bob")
    else:
        print("Alice")


for _ in range(T):
    solve()
