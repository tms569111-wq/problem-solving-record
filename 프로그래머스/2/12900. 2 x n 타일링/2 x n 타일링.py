def solution(n):
    # 전부 가로, 전부 세로, 짝수면 n/2 씩하면서 개 수 늘림...
    # dp 써야 하나...
    # n=1일 때 1개
    # n=2일 때 2개
    # n=3일 때 3개
    #n=4일 때 5개
    # 이거 피보나치인가???
    a=0
    b=1
    c=0
    for i in range(n+1):
        c=(a+b)%1000000007
        a,b=c,(a)%1000000007
    
    answer = c
    return answer