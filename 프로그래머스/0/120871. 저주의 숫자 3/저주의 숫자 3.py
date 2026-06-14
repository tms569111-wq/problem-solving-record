def solution(n):
    answer=[]
    count=n
    i=0
    while True:
        i=i+1
        if i%3!=0 and '3' not in str(i):
            answer.append(i)
        else:
            count=count+1
        count=count-1
        if count==0:
            return answer[-1]