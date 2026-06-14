def solution(price, money, count):
    count_1=1
    for i in range(count):
        money-=price*count_1
        count_1+=1
        
    if money>=0:
        return 0
    return money*-1