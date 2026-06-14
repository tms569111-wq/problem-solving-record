def solution(my_string, is_prefix):
    for i in range(0,len(my_string)):
        if is_prefix==my_string[:i+1]:
            return 1
        
    answer = 0
    return answer