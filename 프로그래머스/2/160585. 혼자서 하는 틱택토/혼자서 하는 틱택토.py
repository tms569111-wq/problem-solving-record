from collections import Counter
def solution(board):
    # 먼저 선공의 숫자가 후공보다 같거나 1개 많아야 됨. 그외는 전부 안 됨
    # 만약 선공이 빙고를 했다면 후공은 한개 적어야만 함
    # 만약 후공이 빙고를 했다면 선공은 같아야만 함
    # 빙고가 여러개, O빙고가 여러개 있는 경우도 있을 수 있지만
    # 일단 한 개 빙고가 있으면 상대는 빙고 없어야 함
    num_O = 0
    num_X = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                num_O += 1
            elif board[i][j] == 'X':
                num_X += 1
    if num_O != num_X:
        if num_O != num_X + 1:
            return 0
    # 빙고 체크
    check_O = [0, 0, 0, 0, 0, 0, 0, 0]
    check_X = [0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in range(3):
        if board[i][0] == 'O':
            check_O[0] += 1
        elif board[i][0] == 'X':
            check_X[0] += 1
        if board[i][1] == 'O':
            check_O[7] += 1
        elif board[i][1] == 'X':
            check_X[7] += 1
        if board[1][i] == 'O':
            check_O[6] += 1
        elif board[1][i] == 'X':
            check_X[6] += 1
        
        
        if board[i][2] == 'O':
            check_O[1] += 1
        elif board[i][2] == 'X':
            check_X[1] += 1
        
        if board[0][i] == 'O':
            check_O[2] += 1
        elif board[0][i] == 'X':
            check_X[2] += 1
        
        if board[2][i] == 'O':
            check_O[3] += 1
        elif board[2][i] == 'X':
            check_X[3] += 1
    
        if board[i][2-i] == 'O':
            check_O[4] += 1
        elif board[i][2-i] == 'X':
            check_X[4] += 1
            
        if board[i][i] == 'O':
            check_O[5] += 1
        elif board[i][i] == 'X':
            check_X[5] += 1
    
    bingo_O = 0
    bingo_X = 0
    
    for num in check_O:
        if num == 3:
            bingo_O += 1
    for num in check_X:
        if num == 3:
            bingo_X += 1
    
    if bingo_O != 0 and bingo_X != 0:
        return 0
    
    if bingo_O != 0 and bingo_X == 0:
        if num_O != num_X + 1:
            return 0
        
    if bingo_O == 0 and bingo_X != 0:
        if num_O != num_X:
            return 0
    return 1