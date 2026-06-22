from collections import deque
def solution(storage, requests):
    # 먼저 영어가 1개만 오는 경우랑 2개가 오는 경우를 나눠야 한다.
    # 2개가 오는 경우는 모든 부분을 싹 다 지워야 하는데 이건 그닥 어렵지 않아 보인다.
    # 문제는 1개가 올 때인데 접근 가능해 진다는 점이 참으로 모호하다. 
    # 일단 상하 좌우에서 공백이면 넘어가고 아니면 check 하는 것 까지는 ok
    # 근데 이미 바깥이 비어 있는 경우가 너무 애매하다. 
    # 비어있는 경우가 상하좌우 중 한 곳이 비어있다고 가정할 수도 없는 게 사이가 쏙 빠져나온 경우는
    # 안 됨. 차라리 dfs로 바깥으로 나갈 수 있으면 가능하다고 하기
    # 근데 dfs로 하면 기하 급수적으로 늘어날 것 같은 느낌
    # 일단 해볼까.
    # 해봤자 50*50 * 100 정도라서 25만번 밖에 안 되니까, 여기다 dfs 하면...시간이 넘기려나.
    
    n = len(storage)
    m = len(storage[0])
    
    # 창고 바깥을 표현하기 위해 테두리를 빈 공간 "."으로 감싼다.
    board = [["."] * (m + 2)]
    
    for row in storage:
        board.append(["."] + list(row) + ["."])
    
    board.append(["."] * (m + 2))
    
    rows = n + 2
    cols = m + 2
    
    def forklift(target):
        visited = [[False] * cols for _ in range(rows)]
        q = deque()
        q.append((0,0))
        visited[0][0] = True
        remove_list = []
        
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    continue
                if visited[nx][ny]:
                    continue
                if board[nx][ny] == ".":
                    visited[nx][ny] = True
                    q.append((nx, ny))
                elif board[nx][ny] == target:
                    visited[nx][ny] = True
                    remove_list.append((nx, ny))
                    
        for x, y in remove_list:
            board[x][y] = "."
    def crane(target):
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if board[i][j] == target:
                    board[i][j] = "."
    for req in requests:
        target = req[0]
        
        if len(req) == 2:
            crane(target)
        else:
            forklift(target)
    answer = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if board[i][j] != ".":
                answer += 1
    return answer
                    