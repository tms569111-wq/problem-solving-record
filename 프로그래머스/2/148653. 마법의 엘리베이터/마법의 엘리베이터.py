def solution(storey):
    answer=0
    while storey>0:
        
        digit=storey%10
        if digit<5:
            answer+=digit
            storey=storey//10
        elif digit>5:
            answer+=10-digit
            storey=storey//10+1
        elif digit==5:
            ten_digit=(storey//10)%10
            if ten_digit>=5:
                answer+=10-digit
                storey=storey//10+1
            else:
                answer+=digit
                storey=storey//10
                
    return answer