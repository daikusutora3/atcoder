def has_directed_cycle(graph, starts=None):
    """計算量: 時間 O(V + E + S)、追加空間 O(V)。V は頂点数、E は辺数、S は starts の要素数（省略時 V）。

    Source: https://github.com/daikusutora3/atcoder
    """
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
    """計算量: 時間 O(V + E + S)、追加空間 O(V)。V は頂点数、E は辺数、S は starts の要素数（省略時 V）。

    Source: https://github.com/daikusutora3/atcoder
    """
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
