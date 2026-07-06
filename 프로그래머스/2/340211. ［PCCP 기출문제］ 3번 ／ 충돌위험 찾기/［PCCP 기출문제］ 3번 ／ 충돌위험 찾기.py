def solution(points, routes):
    # 매초마다 1만개를 업데이트 하는 건 시간이 오바 될 수 있음
    # 각 루트의 로봇들이 100개 100개가 100번 움직인다고 하면 1만번
    # 중복 없고 움직이는 크기가 맨해튼 거리 최악으로 200이니까 200만번
    # 즉 각 로봇들을 움직이게 시켜야 함
    # 일단 각 로봇들의 상태를 false라고 함
    # crash난 걸 표시하고 확인해야 하는데 로봇이 100개 임
    # 만약 crash가 99번 안 나고 1개 나면
    # stack으로 구하면 시간 오바 될 정도로 너무 많을 듯.
    # True, False로 구해도 100번은 연산해야 하지 않나...2억번 연산해야 될 것 같은데 애매하다
    # 일단 도전!
    answer = 0
    crash_stack = []
    visited = [[False for _ in range(102)] for _ in range(102)]
    end_num = 0
    num = len(routes)
    now = [1] * num
    now_position = [points[routes[i][0] - 1].copy() for i in range(num)]
    next_position = [points[routes[i][1] - 1].copy() for i in range(num)]
    def crash_check(i, new):
        if visited[new[0]][new[1]] == True:
            if new not in crash_stack:
                crash_stack.append(new)
        else:
            visited[new[0]][new[1]] = True
        return
    # 만약 각 num값이 각 루트의 마지막 루트 개수만큼 커지면
    # end_num += 1
    for i in range(num):
        crash_check(i, now_position[i])
    answer += len(crash_stack)
    for x, y in now_position:
        visited[x][y] = False
        crash_stack = []
        
    while end_num != num:
        # 로봇 개수 만큼이면 걸러버리기
        for i in range(num):
            if now[i] == len(routes[i]):
                continue
            # 이동
            if now_position[i][0] < next_position[i][0]:
                now_position[i][0] += 1
                crash_check(i, now_position[i])
            elif now_position[i][0] > next_position[i][0]:
                now_position[i][0] -= 1
                crash_check(i, now_position[i])   
            else:
                if now_position[i][1] > next_position[i][1]:
                    now_position[i][1] -= 1
                    crash_check(i, now_position[i])   
                elif now_position[i][1] < next_position[i][1]:
                    now_position[i][1] += 1
                    crash_check(i, now_position[i])
                    
            if now_position[i][0] == next_position[i][0] and now_position[i][1] == next_position[i][1]:
                now[i] += 1
                if len(routes[i]) == now[i]:
                    end_num += 1
                elif len(routes[i]) > now[i]:
                    next_position[i][0] = points[routes[i][now[i]] - 1][0]
                    next_position[i][1] = points[routes[i][now[i]] - 1][1]
                    
        
        answer += len(crash_stack)
        for x, y in now_position:
            visited[x][y] = False
        crash_stack = []
    
    return answer