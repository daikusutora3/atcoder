N = int(input())
a = list(map(int, input().split()))

ma = 0
mi = 0
for i in range(N):
    if abs(ma) < abs(a[i]):
        ma = a[i]
        mi = i

ans = []
if ma >= 0:
    for i in range(N):
        ans.append((mi + 1, i + 1))
        ans.append((mi + 1, i + 1))
        mi = i
else:
    for i in range(N - 1, -1, -1):
        ans.append((mi + 1, i + 1))
        ans.append((mi + 1, i + 1))
        mi = i

for x, y in ans:
    a[y - 1] += a[x - 1]

print(len(ans))
for a in ans:
    print(*a)
