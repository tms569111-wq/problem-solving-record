def solution(number, limit, power):
    
    answer = 0
    for i in range(1,number+1):
        check=0
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                if j * j == i:
                    check += 1
                else:
                    check += 2
        if check>limit:
            answer+=power
        else:
            answer+=check
    return answer