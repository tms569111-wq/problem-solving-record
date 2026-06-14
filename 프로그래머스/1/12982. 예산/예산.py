def solution(d, budget):
    check=0
    for i in range(len(d)):
        if d==[]:
            break
        z=min(d)
        
        if budget>=z:
            budget-=z
            d.remove(z)
            check+=1
        else:
            return check
    return check