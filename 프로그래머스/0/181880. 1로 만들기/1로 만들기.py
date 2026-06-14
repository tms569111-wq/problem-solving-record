def solution(num_list):
    answer = 0
    for i in num_list:
        while True:
            
            if i==1:
                break
            elif i%2==0:
                i=i//2
            else:
                i=(i-1)//2
            answer+=1    
    return answer