def solution(dots):
    answer=[]
    for i in range(3,0,-1):
        for j in range(i):
            answer.append(abs(abs(dots[i][0]-dots[j][0])+abs(dots[i][1]-dots[j][1])))
            
    answer.sort()
    a=answer[0]*answer[2]
        
    return a