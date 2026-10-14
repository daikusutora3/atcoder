import sys
from collections import deque

N, D = map(int, input().split())
X, Y = map(int, input().split())

x = abs(X // D)
y = abs(Y // D)
if N - x - y < 0 or (N - x - y) % 2 == 1 or X % D != 0 or Y % D != 0:
    print(0)
    sys.exit()

cnt = 0
for a in range(0, N - x - y + 1, 2):
    b = N - x - y - a
    a //= 2
    b //= 2
    # print(f"↑{x}, →{y}, ↑↓{a}, →←{b}, {x + y + (a + b) * 2}")
    res = 1
    waru = []
    for i in range(2, x + a + 1):
        waru.append(i)
    for i in range(2, a + 1):
        waru.append(i)
    for i in range(2, b + 1):
        waru.append(i)
    for i in range(2, y + b + 1):
        waru.append(i)
    waru.sort()
    waru = deque(waru)
    for i in range(2, N + 1):
        res *= i
        if len(waru) > 0 and res % waru[0] == 0:
            res //= waru[0]
            waru.popleft()
    cnt += res

BASE = 10**10
cnt *= BASE
for i in range(N):
    cnt //= 4
cnt /= BASE


print(cnt)
