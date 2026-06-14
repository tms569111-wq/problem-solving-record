def solution(t, p):
    arr=[]
    a=len(p)
    p=int(p)
    answer = 0
    
    for i in range(len(t)-a+1):
        if int(t[i:i+a])<=p:
            answer+=1
        
    return answer