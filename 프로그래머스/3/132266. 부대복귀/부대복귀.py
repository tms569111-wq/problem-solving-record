from collections import deque
def solution(n, roads, sources, destination):
    # 걸리는 시간이 동일하다면 일단...bfs를 고려
    # 최단 시간 부대 복귀
    # 배열
    # 지역인 destination을 start지점으로 생각하고, sources를 다 거쳐야 한다.
    # sources를 다 거치는 길...
    # 이거 연습문제에서 어디 들렸다가 가는 문제랑 비슷하나...
    # 그건 sources가 2개밖에 안 되었는데 여기서는 sources가 500개까지....
    # 아니네 문제 잘 못 읽었다...
    # 각 애들이 부대로 복귀하는 내용이구나...
    
    answer = []
    graph=[[] for i in range(n+1)]
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    dist=[-1]*(n+1)
    q = deque()
    q.append(destination)
    dist[destination] = 0
    
    while q:
        now=q.popleft()
        for next_node in graph[now]:
            if dist[next_node]==-1:
                dist[next_node]=dist[now]+1
                q.append(next_node)

    
    for source in sources:
        answer.append(dist[source])
        
    
    return answer