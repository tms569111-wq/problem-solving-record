def solution(n):
    check=0
    for i in range(1,n+1):
        a=i
        for j in range(i+1,n+1):
            a=a+j
            if a>=n:
                break
        
        if a==n:
            check+=1
        
                
    answer = check
    return answer