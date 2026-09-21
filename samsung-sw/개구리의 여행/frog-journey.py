import heapq

T = int(input())

board = [list(input()) for _ in range(T)] 

travel = int(input())


jump = [[0] * 6 for _ in range(6)]
for i in range(1, 6):
    new = []
    for j in range(1, 6):
        if j < i:
            jump[i][j] = 1
        elif j == i:
            jump[i][j] = 0
        else:
            cost = 0
            for p in range(i + 1, j + 1):
                cost += p * p
                jump[i][j] = cost
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]


def dijkstra(start_x, start_y, end_x, end_y):
    heap = []
    dist = [[[1e9] * 6 for i in range(T)] for _ in range(T)]
    dist[start_x][start_y][1] = 0
    heapq.heappush(heap, (0, start_x, start_y, 1))

    while heap:
        cost, now_x, now_y, power = heapq.heappop(heap)

        # 비용이 커봤자 넘김
        if cost > dist[now_x][now_y][power]:
            continue
        
        if now_x == end_x and now_y == end_y:
            return cost
        
        # cost모든 경우 따짐
        for i in range(1, 6):
            for j in range(4):
                nx = now_x + dx[j] * i
                ny = now_y + dy[j] * i

                # 범위 바깥 체크
                if nx < 0 or ny < 0 or ny >= T or nx >= T:
                    continue
                
                # 미끄러운지 뱀인지
                if board[nx][ny] != '.':
                    continue
                
                # 뱀
                check = 0
                new_x = now_x
                new_y = now_y
                for _ in range(i):
                    new_x = new_x + dx[j]
                    new_y = new_y + dy[j]
                    if board[new_x][new_y] == '#':
                        check = 1
                        break
                if check == 1:
                    continue

                new_cost = cost + 1 + jump[power][i]
                

                if dist[nx][ny][i] > new_cost:
                    dist[nx][ny][i] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny, i))
                

for _ in range(travel):
    r1, c1, r2, c2 = map(int, input().split())
    num = dijkstra(r1 - 1, c1 - 1, r2 - 1, c2 -1)
    if  num == None:
        print(-1)
    else:
        print(num)
                    

        

