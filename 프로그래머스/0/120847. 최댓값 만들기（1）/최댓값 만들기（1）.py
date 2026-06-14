def solution(numbers):
    max_1=max(numbers)
    numbers.remove(max_1)
    max_2=max(numbers)
    answer = max_1*max_2
    return answer