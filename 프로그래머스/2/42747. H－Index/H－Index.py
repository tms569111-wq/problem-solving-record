def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    if len(citations)==1 and citations[0]==0:
        return 0
    elif len(citations)==1 and citations[0]==1:
        return 1
    for i in range(len(citations)):
        if citations[i]>=(i+1):
            continue
        else:
            return i
    
    return len(citations)