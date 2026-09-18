import heapq
def solution(board):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n = len(board)
    dist = [[[int(1e9) for _ in range(4)] for _ in range(n)] for _ in range(n)]
    heap = []
    
    dist[0][0][1] = 100
    heapq.heappush(heap, (100, 0, 0, 1))
    dist[0][0][3] = 100
    heapq.heappush(heap, (100, 0, 0, 3))

        
    while heap:
        cost, x, y, d = heapq.heappop(heap)
        
        if dist[x][y][d] < cost:
            continue
            
        if x == n - 1 and y == n - 1:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
                continue
                
            if i == d:
                new_cost = cost + 100
            else:
                new_cost = cost + 600
                
            if new_cost > dist[nx][ny][i]:
                continue
            else:
                dist[nx][ny][i] = new_cost
                heapq.heappush(heap, (new_cost, nx, ny, i))
        
                    
    return min(dist[n-1][n-1]) - 100
                    
            