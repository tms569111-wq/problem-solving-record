from collections import deque
def solution(maps):
    
    # bfs나 dfs
    # 그런데 dfs는 안 될 것 같은게 파이썬은 깊이가 제한 되어 있음
    # bfs 해야 함.
    # bfs로 x면 넘어가고,,,x아니면 visited면 넘어가도록 한다
    # 숫자들은 그냥 서로 더하고 갈 곳이 없으면 탈출
    
    answer = []
    
    m = len(maps)
    n = len(maps[0])
    
    visited = [[False for _ in range(n)] for _ in range(m)]
    
    # 일단 bfs
    def bfs(i, j):
        q = deque()
        q.append((i,j))
        
        total = int(maps[i][j])
        visited[i][j] = True
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while q:
            row, column = q.popleft()
            
            for i in range(4):
                nx = row + dx[i]
                ny = column + dy[i]
                
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if maps[nx][ny] == 'X' or visited[nx][ny] == True:
                    continue
                visited[nx][ny] = True
                total += int(maps[nx][ny])
                q.append((nx,ny))
        return total
    for i in range(m):
        for j in range(n):
            if maps[i][j] != 'X' and visited[i][j] == False:
                answer.append(bfs(i,j))
    answer.sort()
    
    if answer:
        return answer
    return [-1]