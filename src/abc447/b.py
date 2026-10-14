from collections import defaultdict


S = input()

d = defaultdict(int)
for s in S:
    d[s] += 1

delete_kouho = []
max_num = 0
for s in d.keys():
    if max_num < d[s]:
        max_num = d[s]
        delete_kouho = [s]
    elif max_num == d[s]:
        delete_kouho.append(s)

# print(delete_kouho)

ans = ""
for s in S:
    if s not in delete_kouho:
        ans += s

print(ans)
