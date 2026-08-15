# 200만 에다가 a도 30만이기 때문에 그냥 무식하게 계산하기에는 문제가 많아보임
# 근데 사실 생각해보면 간단한 게 끝에 있는 것들은 연결된 거 1개를 제외하면 방법이 없으므로
# 걍 끝에있는 것들 모두 0으로 하고 그 뒤에 연결 된 것들 0으로 하고 이거 반복하면
# 되긴 할 텐데
# 끝에 있는지 아닌지를 어떻게 아느냐가 중요할 것 같다.
# 일단 그래프로? 
# 끝에 있는 것들은 전부 처리한다면..
# 흠...내 생각에는 bfs 느낌
# 먼저 끝에 있는 것들(해쉬 value가 0인 놈)들을 0으로 하고 그것과 연결된 것들을
# 다 가져오고 끝인 놈들을 다 하면 끝에서 한 칸 위를 다 하는 거고
# 계속 반복...

from collections import deque
def solution(a, edges):
    n = len(a)
    if sum(a) != 0:
        return -1
    
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    parent = [-1] * n
    
    order = []
    
    q = deque([0])
    parent[0] = 0
    while q:
        now = q.popleft()
        order.append(now)
        for nxt in graph[now]:
            if parent[nxt] != -1:
                continue
            parent[nxt] = now
            q.append(nxt)
    weight = a[:]
    answer = 0
    for now in reversed(order[1:]):
        p = parent[now]
        
        answer += abs(weight[now])
        weight[p] += weight[now]
        weight[now] = 0
    return answer
    