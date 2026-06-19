import heapq

def solution(board):
    # bfs같은데 
    # 비용이 중요 한 듯 
    # dp 느낌으로 비용이 저장된 값보다 넘으면 탐색 중단하고 나가게 하기 
    # 근데 이러면 dfs가 더 나은 것 같기도 하고 
    # 일단 head를 만들고 자기가 가고 있는 방향과 다르면 cost를 500으로 하면 될 듯 
    # 이런... 이거 bfs 하면 가장 먼저 도달한 최단거리만 반환 하네... 
    # 다익스트라구나
    
    
    n = len(board)
    INF = 1e9
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    cost_table = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    
    pq = []
    
    heapq.heappush(pq, (0, 0, 0, -1))
    
    while pq:
        cost, x, y, prev_dir = heapq.heappop(pq)
        if prev_dir != -1 and cost > cost_table[x][y][prev_dir]:
            continue
        for next_dir in range(4):
            dx, dy = directions[next_dir]
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >=n or ny < 0 or ny >=n:
                continue
            if board[nx][ny] == 1:
                continue
            if prev_dir == -1:
                new_cost = cost + 100
            elif prev_dir != next_dir:
                new_cost = cost + 600
            else:
                new_cost = cost + 100
            if new_cost < cost_table[nx][ny][next_dir]:
                cost_table[nx][ny][next_dir] = new_cost
                heapq.heappush(pq, (new_cost, nx, ny, next_dir))
    return min(cost_table[n-1][n-1])
            
    