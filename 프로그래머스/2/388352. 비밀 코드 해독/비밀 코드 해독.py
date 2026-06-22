from itertools import combinations
def solution(n, q, ans):
    # 감도 안 오는 문제...
    # 일단 주어진 조건에서 
    # 어떤 숫자 5개 q[0] 2개가 포함되어 있다고 하면
    # 5c4가 5, 5c5는 1 5C2인가 한 10개 가능 근데 q와 m의 길이가 10개 내외이므로
    # 10^10승 정도인가... 10000000000
    # 최악은 100억이긴 한데 일단 조합하다 보면 많이 버려지므로 시간 복잡도는 아주 널널 함
    # 중요한 건 정확도!!!
    # 완전탐색이 정답인듯?
    # 먼저 q[0]에서 2개가 있다면 가능 한 모든 조합
    # 일단 2, 3을 골랐다고 하고 6, 7, 8을 골랐다고 하면, 3, 7, 8, 9는 9가 6개로 5를 넘어가므로 탈락
    # 이거 dfs같다. 
    answer = 0
    q_sets = []
    for query in q:
        q_sets.append(set(query))
    for candidate in combinations(range(1, n + 1), 5):
        candidate_set = set(candidate)
        
        possible = True
        
        for query_set, expected in zip(q_sets, ans):
            if len(candidate_set & query_set) != expected:
                possible = False
                break
        if possible:
            answer += 1
    return answer