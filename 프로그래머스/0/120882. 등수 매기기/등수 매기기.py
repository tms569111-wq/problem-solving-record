def solution(score):
    answer = []
    a=[]
    for i in score:
        answer.append(i[0]+i[1])
    for i in answer:
        count=1
        for j in answer:
            if i<j:
                count+=1
        a.append(count)
    return a
