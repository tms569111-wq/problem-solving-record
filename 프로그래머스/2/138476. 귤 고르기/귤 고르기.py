from collections import Counter
def solution(k, tangerine):
    a=Counter(tangerine)
    z=sorted(a.values(),reverse=True)
    answer=0
    for i in range(0,len(z)):
        answer+=z[i]
        if answer>=k:
            return i+1
    return answer