def solution(s):
    s=s[2:-2].split("},{")
    answer=[]
    s.sort(key=len)
    for i in s:
        z=i.split(',')
        for j in z:
            if int(j) not in answer:
                answer.append(int(j))
    return answer
    