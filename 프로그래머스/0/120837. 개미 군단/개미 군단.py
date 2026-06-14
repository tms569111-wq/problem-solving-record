def solution(hp):
    count=0
    count=int(hp/5)
    hp=hp-int(hp/5)*5
    if hp/3>=1:
        count=count+1
        if hp>0:
            count=count+(hp-3)
    else:
        count=count+hp
    
    return count