#
#필요한 증명 : 트리에서 임의의 노드에서 최대 거리에 있는 노드는 반드시 트리의 지름의 양 끝점 중 하나이다.
#트리는 사이클이 없다
import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
V = int(input())
graph = [[0, -1]]
for _ in range(V):
    graph.append(list(map(int, input().split())))

def dijkstra(start):
    dist = [INF]*(V+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        d, v = heapq.heappop(q)
        if d > dist[v]:
            continue
        for i in range(1, len(graph[v])-1, 2):
            next_v = graph[v][i]
            next_d = graph[v][i+1] + d
            if next_d < dist[next_v]:
                dist[next_v] = next_d
                heapq.heappush(q, (next_d, next_v))
    for i in range(len(dist)):
        if dist[i] == INF:
            dist[i] = -1
    return dist

ds1 = dijkstra(1)
idx = ds1.index(max(ds1))
print(max(dijkstra(idx)))