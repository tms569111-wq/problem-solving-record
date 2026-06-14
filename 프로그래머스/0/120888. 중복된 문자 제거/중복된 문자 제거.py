def solution(my_string):
    check=[]
    answer = ''
    for i in my_string:
        if i not in check:
            check.append(i)
    a="".join(check)
    return a