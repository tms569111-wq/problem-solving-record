def solution(n):
    a=0
    if n%2==1:
        for i in range(n+1):
            if i%2==1:
                a=a+i
    else:
        if n%2==0:
            for i in range(n+1):
                if i%2==0:
                    a=a+i**2
    return a