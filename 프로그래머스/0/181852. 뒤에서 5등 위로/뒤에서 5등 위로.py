def solution(num_list):
    for i in range(5):
        num_list.remove(min(num_list))
    num_list.sort()
    return num_list