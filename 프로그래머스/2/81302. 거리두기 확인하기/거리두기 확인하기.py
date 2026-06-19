from collections import deque
def solution(places):
    answer = []
    
    # 각 places에서 bfs를 하고, 한 점에서 다른 점 까지의 거리가 맨해튼 거리 2인지 체크
    # 수가 적어서 시간초과는 생각 안 하고 완전탐색 느낌으로 풀어보자
    # 카카오는 약간 다 이런 느낌인가???
    def bfs(i, j, wait):
        q = deque()
        visited = [[False for _ in range(len(wait[0]))] for _ in range(len(wait))]
        q.append((i, j, 0))
        visited[i][j] = True
        dx = [-1, 1, 0 ,0]
        dy = [0, 0, -1, 1]
        while q:
            x, y, distance = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]        
                if nx < 0 or nx >= len(wait) or ny < 0 or ny >= len(wait[0]):
                    continue
                elif wait[nx][ny] == "X" or visited[nx][ny] == True:
                    continue
                elif wait[nx][ny] == "O":
                    q.append((nx, ny, distance + 1))
                elif wait[nx][ny] == "P":
                    if (distance + 1) <= 2:
                        return False
                    else:
                        q.append((nx, ny, distance + 1))
                visited[nx][ny] = True
        return True
    def check(wait):
        for i in range(len(wait)):
            for j in range(len(wait[0])):
                if wait[i][j] == "P":
                    if bfs(i, j, wait) == False:
                        return 0
        return 1
        
        
    for wait in places:
        answer.append(check(wait))
    return answer