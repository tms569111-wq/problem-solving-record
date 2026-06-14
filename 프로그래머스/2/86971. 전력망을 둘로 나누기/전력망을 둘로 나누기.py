from collections import deque

def solution(n,wires):
    answer=n+123
    graph = [[] for _ in range(n + 1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    def bfs(start,cut_a,cut_b):
        visited=[False]*(n+1)
        q=deque()
        q.append(start)
        visited[start]=True
        count=1
        while q:
            now=q.popleft()
            for next_node in graph[now]:
                if now==cut_a and next_node==cut_b:
                    continue
                if now==cut_b and next_node==cut_a:
                    continue
                if not visited[next_node]:
                    visited[next_node]=True
                    q.append(next_node)
                    count+=1
        return count
    for a,b in wires:
        cnt1=bfs(a,a,b)
        cnt2=n-cnt1
        answer=min(answer,abs(cnt1-cnt2))
    return answer
     