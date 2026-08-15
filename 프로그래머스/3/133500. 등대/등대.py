# 문제를 볼 때에 생각
# 일단 그래프라고 되어 있지만 트리처럼 생각하는 게 편할 듯?
# 트리라고 생각하면 루트, 루트 + 2 층, 루트 + 4층 혹은
# 1층, 3층, 5층 ... 이런 식으로 켜두 는 게 아마 유리하겠지
# 근데 또 예시 1보면 그런 건 아닌데
# 흠...그냥 최대로 많이 킬 수 있는 순서대로 키기?
# 이건 근데 최적해를 보장 못 할 것 같지.
# 일단 가장 많이 키는 것들 순서대로 할까
# 자료구조: 그래프(해시)
# 처리순서 : 가장 많이 키는 것들 순서대로
# 상태 : On, off
# 갱신식 : 켜지지 않은 것들 그룹을 두고 가장 많이 켜지는 놈들은 
# 정렬한 뒤 켜진 건 빼고 안 켜진건 냅둠
# 종료조건 : 다 켜질 때 까지...
from collections import deque
def solution(n, lighthouse):
    graph = [[] for _ in range(n + 1)]
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    parent = [-1] * (n + 1)
    parent[1] = 0
    order = []
    q = deque([1])
    while q:
        now = q.popleft()
        order.append(now)
        for nxt in graph[now]:
            if parent[nxt] != -1:
                continue
            parent[nxt] = now
            q. append(nxt)
    dp = [[0, 0] for _ in range(n + 1)]
    for now in reversed(order):
        dp[now][1] = 1
        for nxt in graph[now]:
            if parent[nxt] != now:
                continue
            child = nxt
            dp[now][0] += dp[child][1]
            dp[now][1] += min(dp[child][0], dp[child][1])
        
    return min(dp[1][0], dp[1][1])