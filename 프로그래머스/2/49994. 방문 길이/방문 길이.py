def solution(dirs):
    dp=[]
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    dirc=["L","R","D","U"]
    x=0
    y=0
    answer=0
    for index in dirs:
        
        i=dirc.index(index)
        a,b=x,y
        x+=dx[i]
        y+=dy[i]
        q=[min(a,x),max(a,x),min(b,y),max(b,y)]
        if -5<=x<=5 and -5<=y<=5:
            if q not in dp:
                dp.append(q)
                answer+=1
        else:
            x,y=a,b
    return answer