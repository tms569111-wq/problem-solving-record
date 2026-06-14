def solution(n):
    count=1
    check=0
    for i in range(1,1000):
        if i*count>n:
            return check
            break
        elif i*count<=n:
            count=count*i
            check=check+1
        