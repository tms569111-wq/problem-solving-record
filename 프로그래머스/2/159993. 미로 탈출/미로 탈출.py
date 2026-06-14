from collections import deque
def solution(maps):
    start=lever=end=None
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=="S":
                start=(i,j)
            elif maps[i][j]=="L":
                lever=(i,j)
            elif maps[i][j]=="E":
                end=(i,j)
    
    def bfs(s, e):
        visited=[[False] * len(maps[0]) for _ in range(len(maps))]
        q=deque()
        q.append((s[0],s[1],0))
        visited[s[0]][s[1]]=True
        dx=[-1,1,0,0]
        dy=[0,0,1,-1]
        while q:
            x,y,dist=q.popleft()
            
            if (x,y)==e:
                return dist
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                    if not visited[nx][ny] and maps[nx][ny]!="X":
                        visited[nx][ny]=True
                        q.append((nx,ny,dist+1))
        return -1
        
        
    
    dist1=bfs(start,lever)
    dist2=bfs(lever,end)
    if dist1==-1 or dist2==-1:
        return -1
    return dist1+dist2