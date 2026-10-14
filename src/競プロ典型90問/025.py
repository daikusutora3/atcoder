from collections import defaultdict
from itertools import combinations_with_replacement

N, B = map(int, input().split())

ans = 0
for k in range(1, 13):
    for com in combinations_with_replacement(range(10), k):
        d = defaultdict(int)
        fm = 1
        for c in com:
            fm *= c
            d[c] += 1
        m = B + fm
        if m > N:
            continue
        # 上のmがcomを満たすような数字か？
        while m > 0:
            d[m % 10] -= 1
            m //= 10
        kaisuu = d.values()
        if min(kaisuu) == 0 and max(kaisuu) == 0:
            ans += 1

print(ans)
