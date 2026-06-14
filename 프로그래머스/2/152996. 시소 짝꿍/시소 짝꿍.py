from collections import Counter

def solution(weights):
    count=Counter(weights)

    answer=0
    for w in count:
        c=count[w]
        answer+=c*(c-1)//2

    ratio=[(2,1),(3,2),(4,3)]

    for w in count:
        for a,b in ratio:

            if w*a%b==0:
                target=w*a//b
                if target in count:
                    answer+=count[w]*count[target]

    return answer
