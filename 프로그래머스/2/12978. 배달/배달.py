import heapq

def solution(N, road, K):
    graph=[[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    INF=int(1e9)
    dist=[INF]*(N+1)
    dist[1]=0
    
    heap=[]
    heapq.heappush(heap,(0,1))
    
    while heap:
        cur_dist,now=heapq.heappop(heap)
        if cur_dist>dist[now]:
            continue
        for next_node, cost in graph[now]:
            new_dist=cur_dist+cost
            if new_dist<dist[next_node]:
                dist[next_node]=new_dist
                heapq.heappush(heap, (new_dist, next_node))
                
    answer=0
    
    for d in dist[1:]:
        if d<=K:
            answer+=1
    return answer