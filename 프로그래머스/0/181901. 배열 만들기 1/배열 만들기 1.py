def solution(n, k):
    count=0
    z=k
    answer=[]
    while(k<=n):
        count=count+1
        k=z*count
        if k<=n:
            answer.append(k)
    
    return answer