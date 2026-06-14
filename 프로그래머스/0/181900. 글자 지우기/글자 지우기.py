def solution(my_string, indices):
    a=list(my_string)
    answer=''
    for i in indices:
        a[i]=''
    answer="".join(a)
    return answer