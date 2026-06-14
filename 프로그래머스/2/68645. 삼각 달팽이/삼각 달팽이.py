def solution(n):
    # 삼각형 모양의 2차원 배열을 만든다.
    # n=4이면 [[0], [0,0], [0,0,0], [0,0,0,0]]
    triangle=[[0 for _ in range(i)] for i in range(1, n+1)]
    answer=[]
    # 방향은 아래, 오른쪽, 왼쪽 위 순서로 반복된다.
    # 아래: x + 1, y
    # 오른쪽: x, y + 1
    # 왼쪽 위: x - 1, y - 1
    dx=[1,0,-1]
    dy=[0,1,-1]
    # 시작 좌표는 맨 위 꼭짓점이다.
    x,y=0,0 

    # 처음 방향은 아래쪽이다.
    direction=0

    # 채워야 할 전체 칸 수다.
    _all=n*(n+1)//2
    num=1
    # 1부터 total까지 차례대로 채운다.
    for i in range(_all):
        # 현재 위치에 num을 채운다.
        triangle[x][y]=num

        # 현재 방향으로 다음 좌표를 계산한다.
        nx=x+dx[direction]
        ny=y+dy[direction]
         # 다음 좌표가 범위를 벗어나거나 이미 값이 채워져 있으면 방향을 바꾼다.
        if nx<0 or nx>=n or ny<0 or ny>=len(triangle[nx]) or triangle[nx][ny]!=0:
            # 방향을 아래 → 오른쪽 → 왼쪽 위 순서로 바꾼다.
            direction=(direction+1)%3
            # 방향을 바꾼 뒤, 현재 위치에서 다음 좌표를 다시 계산한다.
            nx=x+dx[direction]
            ny=y+dy[direction]
            

        # 다음 위치로 이동한다.
        num+=1
        x=nx
        y=ny
       
    # 삼각형 배열을 위에서부터 한 줄씩 펼쳐서 answer에 담는다.
    for i in triangle:
        for j in i:
            answer.append(j)
    # 각 행을 하나씩 꺼낸다.


        # 행 안의 값을 하나씩 answer에 추가한다.
    return answer

    # 완성된 1차원 배열을 반환한다.