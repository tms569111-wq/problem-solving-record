# 16개 밖에 안 되고 갔던 곳은 못 가니까
# 완전 탐색 하면 될 듯
# 4 * 4 = 16
# 16 ^ 8 = 196 ^ 4 = 40000 ^ 2 = 16억....
# 완전 탐색 아닌가?
# 레드가 먼저 움직이고 그다음에 블루가 먼저 움직이는 걸로 bfs?
# 아니 dfs가 맞는 듯
# 

def solution(maze):
    answer = [int(1e9)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maze)
    m = len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_goal = (i, j)
            elif maze[i][j] == 4:
                blue_goal = (i, j)

    def dfs(red_now, blue_now, count, visited_red, visited_blue):
        if count >= answer[0]:
            return
        if red_now == red_goal and blue_now == blue_goal:
            if count < answer[0]:
                answer[0] = count
            return
        # 빨강이 갈 수 있는 다음 위치들
        if red_now == red_goal:
            red_nexts = [red_now]
        else:
            red_nexts = []

            for d in range(4):
                nx = red_now[0] + dx[d]
                ny = red_now[1] + dy[d]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maze[nx][ny] == 5:
                    continue
                if visited_red[nx][ny]:
                    continue

                red_nexts.append((nx, ny))
        # 파랑이 갈 수 있는 다음 위치들
        if blue_now == blue_goal:
            blue_nexts = [blue_now]
        else:
            blue_nexts = []

            for d in range(4):
                nx = blue_now[0] + dx[d]
                ny = blue_now[1] + dy[d]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maze[nx][ny] == 5:
                    continue
                if visited_blue[nx][ny]:
                    continue

                blue_nexts.append((nx, ny))
        for red_next in red_nexts:
            for blue_next in blue_nexts:

                # 같은 칸으로 이동 불가
                if red_next == blue_next:
                    continue

                # 서로 자리교환 불가
                if red_next == blue_now and blue_next == red_now:
                    continue

                red_moved = red_next != red_now
                blue_moved = blue_next != blue_now

                if red_moved:
                    visited_red[red_next[0]][red_next[1]] = True

                if blue_moved:
                    visited_blue[blue_next[0]][blue_next[1]] = True
                dfs(
                    red_next,
                    blue_next,
                    count + 1,
                    visited_red,
                    visited_blue
                )

                if red_moved:
                    visited_red[red_next[0]][red_next[1]] = False

                if blue_moved:
                    visited_blue[blue_next[0]][blue_next[1]] = False
    visited_red = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visited_blue = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    visited_red[red_start[0]][red_start[1]] = True
    visited_blue[blue_start[0]][blue_start[1]] = True
    dfs(red_start, blue_start, 0, visited_red, visited_blue)     
    
    return 0 if answer[0] == int(1e9) else answer[0]