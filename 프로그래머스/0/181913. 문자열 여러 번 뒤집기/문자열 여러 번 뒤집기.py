def solution(my_string, queries):
    a=''
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1] = answer[s:e+1][::-1]

    a="".join(answer)

    return a