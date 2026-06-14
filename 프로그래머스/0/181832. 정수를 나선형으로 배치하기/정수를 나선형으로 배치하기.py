def solution(n):
    answer = [[0] * n for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c = 0, 0 
    dir_idx = 0 
    
    for i in range(1, n * n + 1):
        answer[r][c] = i
        nr, nc = r + dr[dir_idx], c + dc[dir_idx]
        if 0 <= nr < n and 0 <= nc < n and answer[nr][nc] == 0:
            r, c = nr, nc
        else:
            dir_idx = (dir_idx + 1) % 4
            r, c = r + dr[dir_idx], c + dc[dir_idx]
            
    return answer