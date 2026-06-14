def solution(board, moves):
    # 바구니는 스택으로 하고 스택[-1]이 새로 들어오려는 놈과 같으면 pop하고 제거
    # board에서 board[x][j]에서 x를 낮춰가면서 체크
    # board[x][j]에서 값이 0이 아닌 놈이 있으면 그 부분 0으로 만들고 바구니에 넣기
    # pop 할 때마다 answer+=1
    # 만약 moves의 값이 len(board)보다 크면 continue
    max_val=len(board)
    stack=[]
    answer = 0
    for move in moves:
        # 값 찾기
        move-=1
        if move>=max_val:
            continue
        for i in range(len(board[move])):
            if board[i][move]!=0:
                if stack==[]:
                    stack.append(board[i][move])
                    board[i][move]=0
                    break
                elif stack!=[] and stack[-1]==board[i][move]:
                    answer+=2
                    board[i][move]=0
                    stack.pop()
                    break
                else:
                    stack.append(board[i][move])
                    board[i][move]=0
                    break
            
    
    return answer