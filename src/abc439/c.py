from collections import defaultdict

N = int(input())

d = defaultdict(int)
x = 1
while x * x < N:
    y = x + 1
    while x * x + y * y <= N:
        d[x * x + y * y] += 1
        y += 1
    x += 1

ans = []
for key, value in d.items():
    if value == 1:
        ans.append(key)

ans.sort()
print(len(ans))
print(*ans)
