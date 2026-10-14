N, W = map(int, input().split())
A = list(map(int, input().split()))

c = [list(map(int, input().split()))[1:] for i in range(N)]

keys = set()
for k in c:
    keys |= set(k)

dag = [[] for i in range(len(keys))]
