from collections import deque
def solution(board):
    # 누가봐도 bfs
    visited=[[False for _ in range(len(board[0]))] for _ in range(len(board))]
    q=deque()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='R':
                start=(i,j)
            elif board[i][j]=='G':
                goal=(i,j)
    q.append((start[0],start[1],0))
    visited[start[0]][start[1]]=True
    m=len(board[0])
    n=len(board)
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    while q:
        x,y,count=q.popleft()
        if (x,y)==goal:
            return count
        for k in range(4):
            nx=x
            ny=y
            while True:
                next_x=nx+dx[k]
                next_y=ny+dy[k]
                if not(0<=next_x<n and 0<=next_y<m):
                    break
                if board[next_x][next_y]=='D':
                    break
                nx=next_x
                ny=next_y
            if not visited[nx][ny]:
                visited[nx][ny]=True
                q.append((nx,ny,count+1))
    
    return -1