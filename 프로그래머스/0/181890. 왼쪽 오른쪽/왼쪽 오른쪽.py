def solution(str_list):
    check=0
    answer=[]
    for i in range(len(str_list)):
        if str_list[i]=='l':
            check=i
            answer=str_list[0:i]
            return answer
        elif str_list[i]=='r':
            check=i
            answer=str_list[i+1:]
            return answer
    return answer