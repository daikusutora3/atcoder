from bisect import bisect_left, bisect_right
from collections import defaultdict


N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(list)

# O(N)解放は持ち帰ってやりましょう
ans = 0
rui = [0]
d[0].append(0)
for r, a in enumerate(A):
    v = rui[-1]+a
    rui.append(v)
    d[v].append(r)
    print(rui, f"d[{K - rui[r+1]}]",d[K - rui[r+1]])
    ans += len(d[K - rui[r+1]])

print(ans)


# rui = [0]
# for a in A:
#     rui.append(rui[-1]+a)

# for i, v in enumerate(rui):
#     d[v].append(i)

# ans = 0
# for l in range(N):
#     br = bisect_right(d[K + rui[l]], l)
#     ans += len(d[K + rui[l]]) - br
