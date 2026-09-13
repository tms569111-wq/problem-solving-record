from functools import lru_cache
def solution(board):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n = len(board)
    visited = [[False for _ in range(n)] for _ in range(n)]
    fee = [[1e9 for _ in range(n)] for _ in range(n)]
    
    @lru_cache(None)
    def dfs(x, y, money, previous):
        if x == n - 1 and y == n - 1:
            if money < fee[n - 1][n - 1]:
                fee[n - 1][n - 1] = money
            return
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == True:
                continue
            if board[nx][ny] == 1:
                continue
            if previous != i:
                visited[nx][ny] = True
                dfs(nx, ny, money + 500 + 100, i)
                visited[nx][ny] = False
            else:
                visited[nx][ny] = True
                dfs(nx, ny, money + 100, i)
                visited[nx][ny] = False
                        
    visited[0][0] = True
    dfs(0, 0, -500, -1)
    return fee[n - 1][n - 1]