from functools import lru_cache
# cost를 2진 dfs로 구하기
# 스테이지를 깨기는 무조건 깨야 하므로
# 스테이지만 깨고 내려가는 경우와
# 스테이지를 깨고 힌트권도 사고 내려가는 경우
# 이렇게 두 개로 나누어서 계산
def solution(cost, hint):
    n = len(cost)
    
    @lru_cache(None)
    def dfs(now, hint_counts):
        
        current_hint_count = hint_counts[now]
        current_hint_count = min(current_hint_count, n - 1)
        
        stage_cost = cost[now][current_hint_count]
        
        if now == n - 1:
            return stage_cost
        
        not_buy = stage_cost + dfs(now + 1, hint_counts)
        
        next_hint_counts = list(hint_counts)
        
        for hint_number in hint[now][1:]:
            stage_index = hint_number - 1
            
            next_hint_counts[stage_index] = min(
                n - 1,
                next_hint_counts[stage_index] + 1
            )
        next_hint_counts = tuple(next_hint_counts)
        buy = (stage_cost + hint[now][0] + dfs(now + 1, next_hint_counts))
        
        return min(not_buy, buy)
    initial_hint_counts = tuple([0] * n)
    return dfs(0, initial_hint_counts)
     