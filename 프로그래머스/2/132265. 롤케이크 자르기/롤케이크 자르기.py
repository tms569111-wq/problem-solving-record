from collections import Counter
def solution(topping):
    brother=Counter(topping)
    me=set()
    brother_kind=len(brother)
    me_kind=0
    answer = 0
    for i in topping:
        if i not in me:
            me.add(i)
            me_kind+=1
        brother[i]-=1
        if brother[i] == 0:
            brother_kind -= 1
        if brother_kind==me_kind:
            answer+=1
    
    return answer