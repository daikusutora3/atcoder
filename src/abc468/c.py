from itertools import permutations


N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))


ans = 0
flag = 0
for p in permutations([i + 1 for i in range(N)]):
    if p == Q:
        flag -= float("inf")
    if flag > 0:
        ans += 1
    if p == P:
        flag += 1
    if p == Q:
        flag -= float("inf")

print(ans)
