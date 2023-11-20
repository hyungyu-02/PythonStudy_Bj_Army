import heapq

list = []
heapq.heappush(list, 2)
heapq.heappush(list, 6)
heapq.heappush(list, 1)
heapq.heappush(list, 3)
heapq.heappush(list, 1)
for i in range(len(list)):
    print(heapq.heappop(list))