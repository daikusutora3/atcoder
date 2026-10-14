from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))


# だいすくらと関数
def dai_sqrt(n):
    ok = 0.0
    ng = 10.0**9
    while ng - ok > 0.01:
        mid = (ok + ng) / 2
        if (n / mid) ** 2 > n:
            ok = mid
        else:
            ng = mid
    return int(ng // 1)  # ここだけ修正（ok -> ng）


base = dai_sqrt(N)
buckets = [defaultdict(int) for bi in range(N // base + (1 if N % base else 0))]

for i in range(N):
    buckets[i // base][A[i]] += 1

Q = int(input())
ans = []
for _ in range(Q):
    L, R, X = map(int, input().split())
    L, R = L - 1, R - 1

    bl = L // base
    br = R // base

    cnt = 0
    if bl == br:
        for i in range(L, R + 1):
            cnt += 1 if A[i] == X else 0
    else:
        for bi in range(bl + 1, br):
            cnt += buckets[bi][X]
        for i in range(L, (bl + 1) * base):
            cnt += 1 if A[i] == X else 0
        for i in range(br * base, R + 1):
            cnt += 1 if A[i] == X else 0

    ans.append(cnt)

print(*ans, sep="\n")
