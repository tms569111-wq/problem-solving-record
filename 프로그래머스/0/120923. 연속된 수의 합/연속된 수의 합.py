def solution(num, total):
    a=total//num
    answer = []
    z=num//2
    if num%2==1:
        for i in range(a-z,a+z+1):
            answer.append(i)
        
    else:
        for i in range(a-z+1,a+z+1):
            answer.append(i)
    
    return answer