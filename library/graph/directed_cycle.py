def has_directed_cycle(graph, starts=None):
    n = len(graph)

    # 0: 未訪問
    # 1: 訪問中
    # 2: 探索完了
    state = [0] * n

    if starts is None:
        starts = range(n)

    for s in starts:
        if state[s] != 0:
            continue

        state[s] = 1
        stack = [[s, 0]]

        while stack:
            v, idx = stack[-1]

            if idx == len(graph[v]):
                state[v] = 2
                stack.pop()
                continue

            to = graph[v][idx]
            stack[-1][1] += 1

            if state[to] == 0:
                state[to] = 1
                stack.append([to, 0])
            elif state[to] == 1:
                return True

    return False


def find_directed_cycle(graph, starts=None):
    n = len(graph)

    # 0: 未訪問
    # 1: 訪問中
    # 2: 探索完了
    state = [0] * n
    parent = [-1] * n

    if starts is None:
        starts = range(n)

    for s in starts:
        if state[s] != 0:
            continue

        state[s] = 1
        parent[s] = -1
        stack = [[s, 0]]

        while stack:
            v, idx = stack[-1]

            if idx == len(graph[v]):
                state[v] = 2
                stack.pop()
                continue

            to = graph[v][idx]
            stack[-1][1] += 1

            if state[to] == 0:
                state[to] = 1
                parent[to] = v
                stack.append([to, 0])
            elif state[to] == 1:
                cycle = [to]
                cur = v

                while cur != to:
                    cycle.append(cur)
                    cur = parent[cur]

                cycle.append(to)
                cycle.reverse()
                return cycle

    return []
