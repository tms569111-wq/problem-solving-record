def solution(n, numlist):      
    new_list = [x for x in numlist if x%n==0 ]
    return new_list