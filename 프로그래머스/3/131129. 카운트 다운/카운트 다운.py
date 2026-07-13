from functools import lru_cache
# 최소 다트로 0점
# 싱글 불
# 선공
# 1 ~ 20까지
# 3배니까 60까지
# 어떤 타겟이 있으면 일단 60보다 작은지 보고
# 60보다 작으면 무조건 1방은 아님
# 3의 배수구나
# 1~20, 2~40 2의 배수 3~60 3의 배수
# 이건 dfs가 맞나
# 아 이건 그냥 계산 하거나 뭐 그러면 안 되네
# 
# 완전탐색 해야 되겠는데
# 근데 한 번 루프에 1~20 ~2 ~40 3 ~ 60을 하니까 60번...
# 좀 무린가...
# 일단 해 보자
# 60보다 크면 고민 시작
def solution(target):
    scores = {}
    for i in range(1, 21):
        scores[i] = max(scores.get(i, 0), 1)
        scores[i * 2] = max(scores.get(i * 2, 0), 0)
        scores[i * 3] = max(scores.get(i * 3, 0), 0)
    scores[50] = 1
    dart_scores = sorted(scores.items())
    INF = float('inf')
    dp = [[INF, -INF] for _ in range(target + 1)]
    dp[0] = [0, 0]
    for now_target in range(1, target + 1):
        for score, single_bull in dart_scores:
            if score > now_target:
                break
            previous_target = now_target - score
            candidate_count = dp[previous_target][0] + 1
            candidate_single_bull = (dp[previous_target][1] + single_bull)
            if candidate_count < dp[now_target][0]:
                dp[now_target] = [candidate_count, candidate_single_bull]
            elif candidate_count == dp[now_target][0] and candidate_single_bull > dp[now_target][1]:
                dp[now_target] = [candidate_count, candidate_single_bull]
                
    return dp[target]