from collections import deque
#어찌 어찌 선만 그리면 길이 딱 2개 밖에 없으므로 간단하게 해결 가능
# 문제는 어떻게 선을 그릴 것인가
# 일단 바깥 선들을 다 그리기
# 그뒤 내부에 위치해있는지 5개를 하나 하나 비교하면서 지우기? 
# 근데 2번째 거 보면 딱히 내부가 아닌데도 지워지긴 함
# 근데 저 내부가 아닌 부분은 굳이 dfs 하면 어차피 조건 바깥이라 상관없긴 할 듯
# 좌표값이 50 정도면 4각형이면 200
# 거의 끝에서 끝이라고 해도
# 2500을 4번을 4번
# 십만 번도 연산 안 하니까 시간복잡도는 매우 여유로움
# 끝에 경계값 처리만 잘 하면 될 듯?
def solution(rectangle, characterX, characterY, itemX, itemY):
    visited_inner = [[False for _ in range(102)] for _ in range(102)]
    visited_outside = [[False for _ in range(102)] for _ in range(102)]
    
    for k in range(len(rectangle)):
        x1, y1, x2, y2 = rectangle[k]
        x1 *= 2
        x2 *= 2
        y1 *= 2
        y2 *= 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if not (i == x1 or i == x2 or j == y1 or j == y2):
                    visited_inner[i][j]  = True
                else:
                    visited_outside[i][j] = True
    answer = []
    itemX *= 2
    itemY *= 2
    characterX *= 2
    characterY *= 2
    
    distance = [
        [-1 for _ in range(102)]
        for _ in range(102)
    ]
    
    queue = deque()
    queue.append((characterX, characterY))
    distance[characterX][characterY] = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    while queue:
        now_x, now_y = queue.popleft()
        
        if now_x == itemX and now_y == itemY:
            return distance[now_x][now_y] // 2
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if not (0 <= nx < 102 and 0 <= ny < 102):
                continue
            if distance[nx][ny] != -1:
                continue
            if not visited_outside[nx][ny]:
                continue
            if visited_inner[nx][ny]:
                continue
            distance[nx][ny] = distance[now_x][now_y] + 1
            queue.append((nx, ny))
                
    