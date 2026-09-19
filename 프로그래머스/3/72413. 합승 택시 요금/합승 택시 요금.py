import heapq
from collections import defaultdict
# 그냥 a최소 b최소에서 가는 길 같을 때까지 더하는 건 애매한 게
# a입장에서 살짝 돌고 b입장에서 살짝 돌아도
# 합쳐서 얘네가 갔다가 내리면 이득인 부분이 존재 가능함
# 어떤지점에서 a로 가는 최소 거리, b로 가는 최소 거리 그리고 s로 가는 최소 거리
# 이 3개를 다 더한 거리
# 가 최소인 점이 정답일 것 같은데...
# 이걸 각각 모든 점에서 하는 것보다
# 차라리 start를 a랑 b로 해서 a_dist, b_dist, s_dist하면 될듯.
# 그뒤 min값을 구한다면?
def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for i, j, k in fares:
        graph[i].append((j, k))
        graph[j].append((i, k))
    answer = 0
    
    def dijkstra(start):
        heap = []
        heapq.heappush(heap, (0, start))
        dist = [1e9] * (n + 1)
        dist[start] = 0
        while heap:
            cost, now = heapq.heappop(heap)
            if cost > dist[now]:
                continue
            for nxt, weight in graph[now]:
                new = weight + cost
                if dist[nxt] <= new:
                    continue
                dist[nxt] = new
                heapq.heappush(heap, (new, nxt))
        return dist
    sum_dist = []
    sum_dist.append(dijkstra(b))
    sum_dist.append(dijkstra(a))
    sum_dist.append(dijkstra(s))
    answer = 1e9
    for i in range(n + 1):
        answer = min(answer, sum_dist[0][i] + sum_dist[1][i] + sum_dist[2][i])
    return answer