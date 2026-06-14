def solution(n):
    sosu=[]
    
    for i in range(2, n+1):
        if n%i==0:
            sosu_count=0
            for j in range(1, n+1):
                if i%j==0:
                    sosu_count+=1
            if sosu_count==2:
                sosu.append(i)
    sosu=set(sosu)
    answer = sorted(sosu)
    return answer