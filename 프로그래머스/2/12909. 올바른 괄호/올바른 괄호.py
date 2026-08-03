def solution(s):
    check_1 = 0
    check_2 = 0
    for i in s:
        if i == '(':
            check_1 += 1
        elif i == ')':
            check_2 += 1
        if check_2 > check_1:
            return False
    if check_1 != check_2:
        return False
    return True