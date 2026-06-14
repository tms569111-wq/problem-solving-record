def solution(rank, attendance):
    answer=[]
    for i in range(len(rank)):
        if attendance[i]==1:
            answer.append(rank[i])
    answer.sort()
    
    return rank.index(answer[0])*10000+100*rank.index(answer[1])+rank.index(answer[2])