from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

d = defaultdict(list)

for i in range(N):
    d[A[i]].append(i)


s = set()
cnt = 0
ans = 0

d_keys = sorted(d.keys(), reverse=True) + [0]
for _ in range(len(d_keys) - 1):
    k = d_keys[_]
    nk = d_keys[_ + 1]
    for i in d[k]:
        s.add(i)
        if i - 1 in s:
            cnt += 1
        if i + 1 in s:
            cnt += 1
    # print(len(s) - cnt, k - nk)
    ans += (len(s) - cnt) * (k - nk)


print(ans)
