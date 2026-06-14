def solution(s):
    check_dif=0
    check_same=0
    new=[]
    answer = 0
    for i in s:
        if i not in new and new==[]:
            check_same+=1
            new.append(i)
        elif i not in new and new!=[]:
            check_dif+=1
        elif i in new:
            check_same+=1
        if check_dif==check_same:
            check_dif=0
            check_same=0
            new=[]
            answer += 1
        
    if new!=[]:
        answer+=1
    return answer