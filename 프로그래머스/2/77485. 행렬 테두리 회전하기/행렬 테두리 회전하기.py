def solution(rows, columns, queries):
    # 헷갈리지만 나눠보면 간단한 듯?
    # 일단 행렬을 만들고
    # 만든 행렬을 시계 방향으로 테두리만 돌려버리는 함수로 돌려버리ㅣ고
    # 테두리 값들 최솟값만 따로 빼놨다가
    # return 하면서 최솟값 리스트로 주기
    
    #일단 행렬
    arr = [[i for i in range(j*columns+1,j*columns+columns+1)] for j in range(0,rows)]
    answer = []
    min_num = 0
    
    # 돌리는 리스트
    def clock_wise_turn(x1, y1, x2, y2, arr):
        temp = 0
        now = arr[x1][y1]
        check = 0
        dx = [0, 1, 0 ,-1]
        dy = [1, 0, -1, 0]
        dx_now = x1
        dy_now = y1
        count = 0
        list_min = 1e9
        move_count = 2 * ((x2 - x1) + (y2 - y1))
        while count < move_count:
            list_min = min(now, list_min)
            check_x = dx_now + dx[check]
            check_y = dy_now + dy[check]
            
            if check_x < x1 or check_x > x2 or check_y < y1 or check_y > y2:
                check += 1
                check %= 4
                dx_now = dx_now + dx[check]
                dy_now = dy_now + dy[check]
            else:
                dx_now = check_x 
                dy_now = check_y
            temp = arr[dx_now][dy_now]
            arr[dx_now][dy_now] = now
            now = temp
            count += 1
        return arr, list_min
    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        arr, min_num = clock_wise_turn(x1, y1, x2, y2, arr)
        answer.append(min_num)
    return answer