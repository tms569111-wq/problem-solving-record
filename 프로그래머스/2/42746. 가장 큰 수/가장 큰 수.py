# 큰수...
# str 사전 순 정렬하면 어떻게 되지?
from functools import cmp_to_key
def solution(numbers):
    str_list = []
    def cmp(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        return 0
    for i in numbers:
        str_list.append(str(i))
    str_list.sort(key = cmp_to_key(cmp))
    answer = ''.join(str_list)
    return '0' if answer[0] == '0'  else answer