from collections import defaultdict
def solution(info, edges):
    # bfs를 한다면...
    # 쭉 내려가는 dfs가 정답일 때 틀림
    # dfs를 한다면 bfs처럼 옆을 돌 때 손해
    # 걍 내려가는 걸 생각하면
    # 2^17 = 4^8 * 2 = 16 ^ 4 * 2  = 256 ^2 * 2 * 대충 10만번
    # 즉 완전탐색 후 모든 탐색에서 양이 제일 많은 경우를 구하는 문제
    # 이때 늑대가 양과 같거나 많으면 바로 break
    # 0부터 시작
    # graph를 먼저 dic으로 만들고
    # 그 뒤 어떻게 해야 하지?
    # 트리를 왔다갔다 하면서 완전탐색...
    # can_go리스트를 만들어서 재귀로 돌리는 게 빠를려나
    answer = []
    def can_go(graph, now, can, sheep, wolf):
        if info[now] == 0:
            sheep += 1
        else:
            wolf += 1
            if wolf >= sheep: 
                answer.append(sheep)
                return
        if now == 0 or can != [] or (can == [] and graph[now]):
            for i in graph[now]:
                can.append(i)
        elif can == []:
            answer.append(sheep)
            return
        
        if can != []:
            for c in can:
                new = [i for i in can if i != c]
                can_go(graph, c, new, sheep, wolf)
    graph = defaultdict(list)
    
    for a, b in edges:
        graph[a].append(b)

    can_go(graph, 0, [], 0, 0)
    return max(answer)