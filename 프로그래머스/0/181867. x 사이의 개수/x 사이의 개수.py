def solution(myString):
    answer=[]
    answer_1 = myString.split('x')

    for i in answer_1:
        answer.append(len(i))
    return answer