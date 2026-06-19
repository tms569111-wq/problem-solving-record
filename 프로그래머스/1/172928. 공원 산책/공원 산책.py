def solution(park, routes):
    # 핵 쉬운데 최적화가 너무 귀찮네.
    # 13분 컷 났는데 걍 돌다가 x나오면 break, 나가면 break 하면 됨
    start_i = 0
    start_j = 0
    m = len(park)
    n = len(park[0])
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start_i = i 
                start_j = j
                break
    for d in routes:
        directions, dis = d.split(" ")
        dis = int(dis)
        check = 0
        nx = start_i
        ny = start_j
        for _ in range(dis):
            if directions == "E":
                ny = ny + 1
                if nx < 0 or ny < 0 or nx >=m or ny >=n:
                    check = 1
                    break
                if park[start_i][ny] == "X":
                    check = 1
                    break
            elif directions == "N":
                nx = nx - 1
                if nx < 0 or ny < 0 or nx >=m or ny >=n:
                    check = 1
                    break
                if park[nx][start_j] == "X":
                    check =1
                    break
            elif directions == "W":
                ny = ny - 1
                if nx < 0 or ny < 0 or nx >=m or ny >=n:
                    check = 1
                    break
                if park[start_i][ny] == "X":
                    check =1
                    break
            elif directions == "S":
                nx = nx + 1
                if nx < 0 or ny < 0 or nx >=m or ny >=n:
                    check = 1
                    break
                if park[nx][start_j] == "X":
                    check =1
                    break
        if check == 0:
            start_i = nx
            start_j = ny
    
    return [start_i, start_j]