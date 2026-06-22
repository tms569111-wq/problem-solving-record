def solution(board, skill):
    # 일단 board를 모두 돌면서 체크할 수 는 없음
    # 100만번을 250000을 곱하느라 불가
    # 근데 skill도 25만이라서 25만 * 범위 딜 고려하면 좀 그럼
    # 다 하는 것 보다 r1부터 c1, r2부터 c2가 같은 것들 끼리 하면 좀 킵되긴 할 텐데
    # 근데 그럴려면 같은 것들 찾아야 함 그게 더 시간 많이 들 수도
    # 일단 정확성 테스트는 널널하니까 해보고 더 좋은 방법이 있음 찾아볼까
    # 역시 시간 초과 남
    # dic에 넣어서 비교?
    # 일단 r1, c1, r2, c2로 두고
    # 얘네 끼리 더하고 빼서 비교하면....
    # 아 근데 문제가 만약 하나도 안 겹치면...
    # 차분 써야 됨
    n = len(board)
    m = len(board[0])
    answer = 0
    acc = [[0] * (m + 1) for _ in range(n + 1)]
    
    for _type, r1, c1, r2, c2, degree in skill:
        if _type == 1:
            value = -degree
        else:
            value = degree
        acc[r1][c1] += value
        acc[r1][c2 + 1] -= value
        acc[r2 + 1][c1] -= value
        acc[r2 + 1][c2 + 1] += value
    
    for i in range(n+1):
        for j in range(1, m + 1):
            acc[i][j] += acc[i][j -1]
    for j in range(m + 1):
        for i in range(1, n + 1):
            acc[i][j] += acc[i - 1][j]
    
    for i in range(n):
        for j in range(m):
            board[i][j] += acc[i][j]
            if board[i][j] >= 1:
                answer += 1
    return answer