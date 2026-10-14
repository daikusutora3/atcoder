"""
2021/01/29
@Yuya Shimizu

ダイクストラ法（ヒープによる優先度付きキューを用いて）
"""

from collections import defaultdict
import heapq


# O(Elog(V))
def dijkstra(edges, num_node, s):
    """経路の表現
    [終点, 辺の値]
    A, B, C, D, ... → 0, 1, 2, ...とする"""
    node = [float("inf")] * num_node  # スタート地点以外の値は∞で初期化
    node[s] = 0  # スタートは0で初期化

    node_name = []
    heapq.heappush(node_name, [0, s])

    while len(node_name) > 0:
        # ヒープから取り出し
        _, min_point = heapq.heappop(node_name)

        # 経路の要素を各変数に格納することで，視覚的に見やすくする
        for factor in edges[min_point]:
            goal = factor[0]  # 終点
            cost = factor[1]  # コスト

            # 更新条件
            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost  # 更新
                # ヒープに登録
                heapq.heappush(node_name, [node[min_point] + cost, goal])

    return node


N, M = map(int, input().split())
graph = [[] for i in range(N)]

d = defaultdict(lambda: defaultdict(lambda: float("inf")))
for _ in range(M):
    a, b, c = map(int, input().split())
    d[a][b] = min(d[a][b], c)

for a in d.keys():
    for b in d[a].keys():
        graph[a - 1].append([b - 1, d[a][b]])

dist = dijkstra(graph, N, 0)
print(dist[N - 1])
