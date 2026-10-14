N, Q = map(int, input().split())
P = list(map(int, input().split()))


graph = [set() for i in range(N)]

for i in range(N - 1):
    graph[P[i] - 1].add(P[i + 1] - 1)
    graph[P[i + 1] - 1].add(P[i] - 1)

head = P[0] - 1
tail = P[-1] - 1


def result():
    global head  # noqa: PLW0602
    ans = [head]
    v = head
    p = -1
    for i in range(N - 1):
        for nv in graph[v]:
            if nv == p:
                continue
            v = nv
        p = ans[-1]
        ans.append(v)
    return ans


for _ in range(Q):
    a = int(input())
    a -= 1
    if N == 1:
        continue
    if a == head:
        head = next(iter(graph[a]))
        graph[head].remove(a)
        graph[tail].add(a)
        graph[a] = {tail}
        tail = a
    elif a == tail:
        pass
    else:
        v1, v2 = list(graph[a])
        graph[v1].remove(a)
        graph[v2].remove(a)
        graph[v1].add(v2)
        graph[v2].add(v1)
        graph[tail].add(a)
        graph[a] = {tail}
        tail = a


ans = result()

print(*[a + 1 for a in ans])
