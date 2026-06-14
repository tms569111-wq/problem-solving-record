def solution(common):
    check=[common[1]-common[0],common[2]-common[1]]
    if check[0]==check[1]:
        return check[0]+common[-1]
    else:
        a=check[1]/check[0]
        return a*common[-1]
    
        