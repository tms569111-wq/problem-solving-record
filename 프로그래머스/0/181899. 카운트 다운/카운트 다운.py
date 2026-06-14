def solution(start_num, end_num):
    answer=[]
    a=[]
    for i in range(end_num,start_num+1):
        answer.append(i)
    answer.reverse()
    return answer