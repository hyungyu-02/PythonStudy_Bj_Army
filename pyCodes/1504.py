#Dijkstra, heapq
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
#
v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    dij = [INF]*(n+1)
    dij[start] = 0
    heapq.heappush(q, (0, start))
    
    fixed = [False]*(n+1)
    while q:
        curDis, curV = heapq.heappop(q)
        fixed[curV] = True
        for nxt, dis in graph[curV]:
            if fixed[nxt]:
                continue
            if dij[nxt] > curDis + dis:
                dij[nxt] = curDis + dis
                heapq.heappush(q, (curDis + dis, nxt))
    return dij

startV1 = dijkstra(v1)
startV2 = dijkstra(v2)
minVal = min(startV1[1]+startV1[v2]+startV2[n], startV2[1]+startV1[v2]+startV1[n])
if minVal >= INF:
    print(-1)
else:
    print(minVal)