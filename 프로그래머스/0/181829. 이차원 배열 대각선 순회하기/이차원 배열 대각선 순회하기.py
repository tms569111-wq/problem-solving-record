def solution(board, k):
    a=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i+j<=k:
                a.append(board[i][j])    
    return sum(a)