def solution(n_str):
    answer = ''
    check=0
    for i in n_str:
        if i!='0':
            check=1
        if check!=0:
            answer=answer+i

    return answer