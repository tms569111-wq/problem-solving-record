def solution(numbers, k):
    num=0
    for i in range(k-1):
        num=(num+2)%(len(numbers))
        
    answer = numbers[num]
    return answer