from collections import defaultdict, deque


N = int(input())

# bitに対応する値のset
d = defaultdict(lambda: -1)
stack = deque()
now = 0
k = 0
for i in range(N):
    event = input()
    if "PUT" == event[:3]:
        _, c = event.split()
        c = int(c)
        stack.append(c)
        now ^= c
    elif "LOOK" == event[:4]:
        print(d[now])
        k += 1
        d[now] = k
    else:
        c = stack.pop()
        now ^= c
