def solution(m,n,board):
    # 문자열 수정이 안 되니까, 문자 리스트로 바꿔준다.
    board=[list(row) for row in board]
    answer=0
    while True:
        remove=set() # 이번 턴에 지워야 할 좌표들을 저장한다.
        
        # 1. 2x2로 같은 블록이 모인 곳을 찾는다.
        for i in range(m-1):
            for j in range(n-1): # 아래칸을 봐야 하므로 m-1까지만 만든다.
                block=board[i][j] # 현재 칸 문자
                
                if block=="0": # 이미 빈칸이면 검사하지 않음
                    continue
                    # 현재칸, 오른쪽, 아래쪽, 오른쪽 아래가 모두 같은지 확인
                if (board[i][j+1]==block and board[i+1][j]==block and board[i+1][j+1]==block):
                    # 바로 지우지 않고, 지워야 할 좌표만 저장한다.
                    remove.add((i,j))
                    remove.add((i,j+1))
                    remove.add((i+1,j))
                    remove.add((i+1,j+1))
        # 지울 블록이 없으면 종료        
        if not remove:
            break
        # 3. 이번 턴에 지워지는 블록 개수 누적
        answer+=len(remove)
        
        # 실제로 블록 지우기
        for i,j in remove:
            board[i][j]="0"
        # 블록 떨어뜨리기
        for j in range(n):
            # 각 열마다 처리
            stack=[] #이 열에서 살아남은 블록들 저장
            
            for i in range(m): # 위에서 아래로 내려가며 확인
                if board[i][j]!="0":
                    stack.append(board[i][j])
            # 위쪽은 빈칸, 아래쪽은 살아남은 블록으로 다시 채운다.
            empty_count=m-len(stack)
            for i in range(empty_count):
                board[i][j]="0"
            for i in range(len(stack)):
                board[empty_count+i][j]=stack[i]
    return answer
            
                    
                    