def solution(n):
    answer=[]
    if(n%2!=1):
        n=n-1
    if(n==1):
        answer.append(1)
        return answer
    else:
        for i in range(1,n+1,2):
            answer.append(i)
        return answer