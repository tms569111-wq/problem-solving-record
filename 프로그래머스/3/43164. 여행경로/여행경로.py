from collections import defaultdict
def solution(tickets):
    # 일단 딱 보니까 깊이 우선 탐색
    # 일단 ICN인 놈으로 시작해서 끝에 도달할 때까지 가야함
    # 그런데??? 또 경로가 여러개 있으면 알파벳 순서가 앞서는 경로를 return
    # 흠...
    # 일단 큐에서 빼내서 오른쪽의 경로가 왼쪽에 있는 걸로 ㄱㄱㄱ
    
    graph=defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    for start in graph:
        graph[start].sort(reverse=True)
    stack=["ICN"]
    route=[]
    while stack:
        now=stack[-1]
        if graph[now]:
            stack.append(graph[now].pop())
        else:
            route.append(stack.pop())
    return route[::-1]