from bisect import bisect_right
from collections import defaultdict


N, K, P = map(int, input().split())
A = list(map(int, input().split()))

# B[k]: 前半で選んだ商品がk個となる価格の合計
B = defaultdict(list)
# C[k]: 後半で選んだ商品がk個となる価格の合計
C = defaultdict(list)

for bit in range(2 ** (N // 2)):
    s = 0
    cnt = 0
    for i in range(N // 2):
        if bit >> i & 1:
            s += A[i]
            cnt += 1
    B[cnt].append(s)

for bit in range(2 ** (N - N // 2)):
    s = 0
    cnt = 0
    for i in range(N - N // 2):
        if bit >> i & 1:
            s += A[N // 2 + i]
            cnt += 1
    C[cnt].append(s)


for b in B.values():
    b.sort()

for c in C.values():
    c.sort()

ans = 0
for bk in range(N // 2 + 1):
    if K - bk < 0:
        continue
    for b in B[bk]:
        # print(f"{bk}個選んでsumが{b}: {C[K - bk]}の中で{P - b}以下の数字の個数")
        br = bisect_right(C[K - bk], P - b)
        # print(br)
        ans += br

print(ans)
