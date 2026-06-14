def solution(board):
    n=len(board)
    a_1=[[1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                for k in range(i-1,i+2):
                    for z in range(j-1,j+2):
                        if 0<=k<n and 0<=z<n:
                            a_1[k][z]=0
    flatten = sum(a_1, [])
    
    answer=sum(flatten)
    return answer