def solution(my_strings, parts):
    answer = ''
    count=0
    
    for s,e in parts:
        z=''
        z=my_strings[count]
        answer=answer+z[s:e+1]
        count=count+1
    return answer