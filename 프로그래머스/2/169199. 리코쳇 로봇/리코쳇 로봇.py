# 갔던 곳을 다시 가는 visited
# visited 한다...
from collections import deque
def solution(board):
    n = len(board)
    m = len(board[0])
    def bfs(now, count):
        visited = [[False for _ in range(m)] for _ in range(n)]
        q = deque([(now, count)])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        while q:
            (x, y) , count = q.popleft()
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if board[nx][ny] == 'D':
                    continue
                while nx >= 0 and ny >= 0 and nx <= n - 1 and ny <= m - 1 and board[nx][ny] != 'D':
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:
                        nx = nx - dx[i]
                        ny = ny - dy[i]
                        break
                    if board[nx][ny] == 'D':
                        nx = nx - dx[i]
                        ny = ny - dy[i]
                        break
                if visited[nx][ny] == True:
                    continue
                else:
                    if board[nx][ny] == 'G':
                        return count + 1
                    visited[nx][ny] = True
                    q.append(((nx, ny), count + 1))
        return -1
                
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                answer = bfs((i, j), 0)
                break
    return answer
    
    