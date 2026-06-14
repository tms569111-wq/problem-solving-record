def solution(n):
    n_0=0
    n_1=1
    n_2=1
    for i in range(n):
        n_2=(n_0+n_1)%1234567
        n_0=(n_1)%1234567
        n_1=n_2
        
    
    answer = n_0
    return answer