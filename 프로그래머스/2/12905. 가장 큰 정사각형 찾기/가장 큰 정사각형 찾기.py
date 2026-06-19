def solution(board):
    # 이거 다른 문제에서 푼 것 같은 느낌
    # 어떤 x에서 오른쪽, 왼쪽, 오른쪽 아래 반복해서 보는 거
    # 근데 배열이 1000임...
    # 뭔가 위쪽에서 한 거랑 겹치면 안 되게 하는 dp가 좋을 것 같은데 어떻게 써야 하나...
    rows = len(board)
    cols = len(board[0])
    max_side = 0
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
                continue
            if i == 0 or j == 0:
                max_side = max(max_side, 1)
                continue
            board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
            max_side = max(max_side, board[i][j])
    return max_side * max_side
            
    