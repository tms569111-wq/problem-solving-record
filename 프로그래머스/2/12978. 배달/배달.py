import heapq
from collections import defaultdict
def solution(N, road, K):
    graph = defaultdict(list)
    for u, v, cost in road:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    
    dist = [1e9 for i in range(N + 1)]
    dist[1] = 0
    heap = [(0, 1)]
    while heap:
        cost, now = heapq.heappop(heap)
        
        if cost > dist[now]:
            continue
        
        for nxt, weight in graph[now]:
            new_cost = weight + cost
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(heap, (new_cost, nxt))
    answer = 0
    for i in range(1, len(dist)):
        if dist[i] <= K:
            answer += 1
    return answer
    