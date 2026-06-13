from collections import deque
def solution(n, edge):
    # 가장 멀리를 알려면, 각 그래프들과 1번 노드 사이의 최단거리를 다 구하면 됨.
    # 어찌보면???? 부대복귀 문제랑 똑같은 느낌.
    # 단 부대복귀는 source만 구했는데 여기는 큰놈들을 구해야 함.
    # 즉, 50000개에서 최대값인 놈과 그놈들 집합도 따로 구해야 함.
    # 복습한다, 이걸 내 유형으로 만들자고 생각하고 해봐야징
    graph=[[] for _ in range(n+1)]
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    dist=[-1]*(n+1)
    q=deque()
    q.append(1)
    dist[1]=0
    while q:
        now=q.popleft()
        for i in graph[now]:
            if dist[i]==-1:
                dist[i]=dist[now]+1
                q.append(i)
    m=max(dist)
    answer=0
    for i in dist:
        if i==m:
            answer+=1
        
                
    return answer