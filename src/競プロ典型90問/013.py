"""
2021/01/29
@Yuya Shimizu

ダイクストラ法（ヒープによる優先度付きキューを用いて）
"""

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

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a - 1].append([b - 1, c])
    graph[b - 1].append([a - 1, c])

dist_1 = dijkstra(graph, N, 0)
dist_2 = dijkstra(graph, N, N - 1)

for k in range(N):
    print(dist_1[k] + dist_2[k])
