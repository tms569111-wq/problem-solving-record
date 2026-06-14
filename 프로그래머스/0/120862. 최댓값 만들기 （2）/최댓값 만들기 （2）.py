def solution(numbers):
    numbers.sort()
    min_1=0
    min_2=0
    max_1=0
    max_2=0
    min_1=numbers[0]
    min_2=numbers[1]
    max_1=numbers[-1]
    max_2=numbers[-2]
    answer = max(min_1*min_2, max_1*max_2,min_1*max_1)
    return answer