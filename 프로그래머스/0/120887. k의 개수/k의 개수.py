def solution(i, j, k):
    k=str(k)
    answer = 0
    for z in range(i,j+1):
        q=str(z)
        for u in q:
            if k in u:
                answer+=1
    
    return answer