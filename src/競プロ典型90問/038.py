from math import lcm


A, B = map(int, input().split())
ans = lcm(A, B)
print("Large" if ans > 10**18 else ans)
