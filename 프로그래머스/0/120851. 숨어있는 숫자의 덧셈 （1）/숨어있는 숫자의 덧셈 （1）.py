def solution(my_string):
    count=0
    for i in my_string:
        if i.isdecimal()==1:
            count=count+int(i)
    return count