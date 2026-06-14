def solution(a, b):
    anser=''
    answer_1= int(str(a)+str(b))
    answer_2=int(str(b)+str(a))
    if answer_1>answer_2:
        return answer_1
    else:
        return answer_2