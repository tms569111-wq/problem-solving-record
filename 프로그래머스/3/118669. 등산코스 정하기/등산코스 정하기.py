from collections import defaultdict
import heapq
# 일단 처음 든 생각은 플로이드 워셜인데
# n이 5만인데 n의 3승이니까 불가능하다
# 다음은 bfs나 dfs인데
# n이 수만개에 봉우리도 수만개...
# lru_cache써도 이건 너무 많이 탐색해야 할 듯
# 그러면 다익스트라?
# 각 출발점에서 산봉우리까지 dp처럼 계산한 다익스트라 같은데
# 일단 그래프를 딕셔너리로 나타내고 
# 어디까지 갈 때 최소값을 업데이트
# 목표값으로 향할 때 이미 업데이트 최소값 한 곳이면 그냥 그 intensity로
# 아 근데 구현이 안되네 help
def solution(n, paths, gates, summits):
    dic = defaultdict(list)
    for node1, node2, time in paths:
        dic[node1].append((node2, time))
        dic[node2].append((node1, time))
    summit_set = set(summits)
    intensity = [float("inf")] * (n + 1)
    heap = []
    
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(heap, (0, gate))
            
        while heap:
            now_intensity, now_node = heapq.heappop(heap)
            if now_intensity > intensity[now_node]:
                continue
            if now_node in summit_set:
                continue
            for next_node, time in dic[now_node]:
                next_intensity = max(now_intensity, time)
                if next_intensity < intensity[next_node]:
                    intensity[next_node] = next_intensity
                    heapq.heappush(heap, (next_intensity, next_node))
    summits.sort()
    answer_summit = summits[0]
    answer_intensity = intensity[answer_summit]
    for summit in summits:
        if intensity[summit] < answer_intensity:
            answer_summit = summit
            answer_intensity = intensity[summit]
                
    return [answer_summit, answer_intensity]