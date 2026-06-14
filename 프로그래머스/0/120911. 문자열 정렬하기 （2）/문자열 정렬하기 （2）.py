def solution(my_string):
    my_string=my_string.lower()
    print(my_string)
    a=list(my_string)
    a.sort()
    a="".join(a)
    return a