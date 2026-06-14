def solution(s):
    answer=[]
    for i in range(len(s)):
        check=0
        for j in range(i-1,-1,-1):
            if s[j]==s[i]:
                a=0
                a=i-j
                answer.append(a)
                check+=1
                break
        if check==0:
            answer.append(-1)
        
    return answer