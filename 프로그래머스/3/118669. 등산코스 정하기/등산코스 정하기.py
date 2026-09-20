from collections import defaultdict
import heapq
# 각 산봉우리에서 다른 산봉우리 안 가고 각각의 출입구로 가는 다익스트라
# 현재 맥스 값보다 작으면 바꾸기로 하기
# 5만이라서 산봉우리가 5만개면 path도 5만이라서 2억 5천...
# 시간이 애매할 것 같은데...

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    dist = [1e9 for i in range(n + 1)]
    heap = []
    
    summit = set(summits)
    gate = set(gates)
    for i in gate:
        heapq.heappush(heap, (0, i))
        dist[i] = 0
    while heap:
        cost, now = heapq.heappop(heap)
        
        if cost > dist[now]:
            continue
        if now in summit:
            continue
            
        for nxt, weight in graph[now]:
            if nxt in gate:
                continue
            
            if dist[nxt] > max(weight, cost):
                dist[nxt] = max(weight, cost)
                
                heapq.heappush(heap, (max(weight, cost), nxt))
    min_num = 1e9
    now = 0
    summits.sort()
    for i in range(len(summits)):
        if dist[summits[i]] < min_num:
            min_num = dist[summits[i]]
            now = i
    return [summits[now], min_num]
            