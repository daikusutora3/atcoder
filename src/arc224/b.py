from math import isqrt


def solve():
    N = int(input())
    a = isqrt(N)
    N -= a
    ans = a - 1
    ans += (N // a) * (2 * a - 1)
    N = N % a
    if N > 0:
        ans += 2 * N - 1
    print(ans)


T = int(input())
for _ in range(T):
    solve()
