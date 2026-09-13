from collections import deque, defaultdict
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
    # 하나하나 하면?
    # 계산 짱 많음.
    # 근데 bfs로 그냥 최단 거리 도달을 다 dp 같은 곳에 넣어 둔다면?
    # 10만? 정도면 끝.
    # bfs는 곂칠 경우 비교해서 덮어 씌울 필요도 없이...
    # 항상 최솟값 보장...
    answer = []
    
    visited = [False for _ in range(n + 1)]
    q = deque([(destination, 0)])
    visited[destination] = True
    board = [-1 for _ in range(n + 1)]
    graph = defaultdict(deque)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    while q:
        now_location, now_distance = q.popleft()
        board[now_location] = now_distance
        while graph[now_location]:
            next_location = graph[now_location].popleft()
            if visited[next_location] == True:
                continue
            else:
                visited[next_location] = True
                q.append((next_location, now_distance + 1))
    for i in sources:
        answer.append(board[i])
    return answer
            