def solution(k, m, score):
    score.sort(reverse=True)
    l=len(score)
    answer=0
    if l<m:
        return 0
    for i in range(m,l+1,m):
        answer+=m*min(score[i-m:i])
    return answer