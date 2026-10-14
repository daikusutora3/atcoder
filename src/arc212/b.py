import heapq
import sys

INF = 10**18

input = sys.stdin.readline
N, M = map(int, input().split())
xyc = [[] for _ in range(M)]
x_to_i = [[] for _ in range(N)]
y_to_i = [[] for _ in range(N)]
for i in range(M):
    x, y, c = map(int, input().split())
    x, y = x - 1, y - 1
    xyc[i] = [x, y, c]
    x_to_i[x].append(i)
    y_to_i[y].append(i)

# ★グラフは「操作M個 + ハブN個」
graph = [[] for _ in range(M + N)]

# 操作 i -> ハブ(x_i) にコスト c_i
for i in range(M):
    x, y, c = xyc[i]
    graph[i].append((M + x, c))

# ハブ(k) -> y=k の操作へ コスト0
for k in range(N):
    hub = M + k
    for v in y_to_i[k]:
        graph[hub].append((v, 0))
"""
2graph21/01/29
@Yuya Shimizu

ダイクストラ法（ヒープによる優先度付きキューを用いて）
"""


def dijkstra(edges, num_node):
    """経路の表現
    [終点, 辺の値]
    A, B, C, D, ... → 0, 1, 2, ...とする"""
    node = [INF] * num_node
    node[0] = 0
    node_name = []
    heapq.heappush(node_name, [0, 0])
    while len(node_name) > 0:
        _, min_point = heapq.heappop(node_name)
        for factor in edges[min_point]:
            goal = factor[0]
            cost = factor[1]
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost
                heapq.heappush(node_name, [node[min_point] + cost, goal])

    return node


dist = dijkstra(graph, N + M)

ans = INF
for v in x_to_i[xyc[0][1]]:
    ans = min(ans, dist[v] + xyc[v][2])

print(ans if ans != INF else -1)
