def solution(name, yearning, photo):
    
    answer=[]
    for i in photo:
        count=0
        for k in range(len(i)):
             for j in range(len(name)):
                    if i[k]==name[j]:
                        count+=yearning[j]
        answer.append(count)
    return answer