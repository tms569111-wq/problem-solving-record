from collections import deque
def solution(land):
    # 이거 누가 봐도 bfs
    # 근데 bfs가 얼마나 들려나? 일단 500 가로
    # 그 다음 세로니까 25000
    # 그 다음 세로마다 bfs로 하면 최악의 경우 25000번
    # 500 곱하기 25000번
    # 125만이라...
    # 근데 True처리 하긴 하니까 그 정돈 아니려나
    # 일단 ㄱㄱㄱㄱ
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)]
    oil_by_col = [0] * m
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 0 or visited[i][j]:
                continue
            q = deque()
            q.append((i,j))
            visited[i][j] = True
            size = 0
            columns = set()
            while q:
                x, y = q.popleft()
                size += 1
                columns.add(y)
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    if land[nx][ny] == 0 or visited[nx][ny]:
                        continue
                    q.append((nx, ny))
                    visited[nx][ny] = True
            for col in columns:
                oil_by_col[col] += size
    return max(oil_by_col)
                        