def solution(keyinput, board):
    direction=['left','right', 'up','down']
    now=[0,0]
    for i in keyinput:
        if i==direction[0] and board[0]//2*(-1)!=now[0]:
            now[0]=now[0]-1
        elif i==direction[1] and board[0]//2!=now[0]:
            now[0]=now[0]+1
        elif i==direction[2] and board[1]//2!=now[1]:
            now[1]=now[1]+1
        elif i==direction[3] and board[1]//2*(-1)!=now[1]:
            now[1]=now[1]-1
    return now