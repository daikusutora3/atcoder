Q = int(input())

d = {}
id = 1

for _ in range(Q):
    s = input()
    if s in d:
        print(d[s])
    else:
        d[s] = id
        print(d[s])
        id += 1
