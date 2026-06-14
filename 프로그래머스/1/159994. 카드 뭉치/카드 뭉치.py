def solution(cards1, cards2, goal):
    check_1=0
    check_2=0
    len_c1=len(cards1)
    
    len_c2=len(cards2)
    for i in range(len(goal)):
        if cards1[check_1]==goal[i]:
            if check_1<len_c1-1:
                check_1+=1
        elif cards2[check_2]==goal[i]:
            if check_2<len_c2-1:
                check_2+=1
                
        else:
            return 'No'
    answer = 'Yes'
    return answer