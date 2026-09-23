# 알고력과 코딩력을 최대한 높일 수 있는
# 그리디로 하면...
# 흠. 또 그렇지는 않군.
# 그러면 어떤 문제를 먼저 풀지 고르는 수열은?
# 문제가 100개라서 100!라 무리...
# 그러면 일단 목표 점 부터 정해야 함
# 제일 알고력 많이 필요한 문제랑
# 제일 코딩력 많이 필요한 문제 두개의 요구사항
# 이걸 목표로 하고
# 그걸 목표로 하되 현재 상황에서
# 경우의 수 1. 코딩 + 1
# 경우의 수 2. 알고 + 1
# 경우의 수 3. 현재 풀 수 있는 문제 중 단위 시간 내로 가장 많이...아 근데
# 3만 올리면 끝인데 100초 걸려서 가장 많이 올리는 거 하면 씹 쌉 손해인데
# 그러면 나머지로 시간 오바되면 가장 가까운 작은 거 순?
# 근데 3만 올리고 나면 다시 엄청 효율 좋은 문제를 풀 수도 있잖아...
# 브루트 포스를 아주 똑똑하게 해야 풀 수 있는 문제야...
# bfs, dfs다 시간 오바 될 것 같고
# dp?
# 근데 어떻게?
# 문제 푸는데 드는 시간이 최대 100초
# 최악의 최악의 경우 문제 푸는데 필요한 알고력과 코딩력 다 1초당 하면 300번 연산
# 문제 푸는 각 시간마다 그때 그때 최단 단위 시간 초마다로 하면...
# 해당 초를 dp로 구하면 각 초에서 도달할 수 있는 최대 알고력과 코딩력 구하고
# 그걸 바탕으로 정답을 못 구하려나...
# 이것도 2개라서 빡세네...
import heapq
def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    
    for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
        max_alp = max(alp_req, max_alp)
        max_cop = max(cop_req, max_cop)
    problems.sort(key = lambda x : (x[0], x[1]))
    def dijkstra(alp, cop):
        answer = 1e9
        heap = [(0, alp, cop)]
        dist = [[1e9 for _ in range(200)] for _ in range(200)]
        dist[alp][cop] = 0
        while heap:
            cost, now_alp, now_cop = heapq.heappop(heap)
            
            if dist[now_alp][now_cop] < cost:
                continue
            
            if now_alp >= max_alp and now_cop >= max_cop:
                if cost < answer:
                    answer = cost
                return answer
            
            if now_alp < 190 and dist[now_alp + 1][now_cop] > cost + 1:
                dist[now_alp + 1][now_cop] = cost + 1
                heapq.heappush(heap, (cost + 1, now_alp + 1, now_cop))
                
            if now_cop < 190 and dist[now_alp][now_cop + 1] > cost + 1:
                dist[now_alp][now_cop + 1] = cost + 1
                heapq.heappush(heap, (cost + 1, now_alp, now_cop + 1))
                
            for alp_req, cop_req, alp_rwd, cop_rwd, weight in problems:
                if now_alp < alp_req:
                    break
                if now_alp >= alp_req and now_cop >= cop_req:
                    new_cost = cost + weight
                    new_alp = min(max_alp, now_alp + alp_rwd)
                    new_cop = min(max_cop, now_cop + cop_rwd)
                    if dist[new_alp][new_cop] > new_cost:
                        dist[new_alp][new_cop] = new_cost
                        heapq.heappush(heap, (new_cost, new_alp, new_cop))
                        
            
            
        return answer
    return dijkstra(alp, cop)
            
        
        