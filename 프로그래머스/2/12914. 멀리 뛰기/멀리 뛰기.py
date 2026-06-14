def solution(n):
    a=1
    b=2
    #피보나치 수열로 구한다
    # f(n)=f(n-1)+f(n-2)
    if n<3:
        return n
    else:
        for i in range(2,n):
            
            a,b=b,(a+b)%1234567
            
            
    
    return b