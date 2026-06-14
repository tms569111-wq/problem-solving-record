def solution(babbling):
    
    answer = 0
    check=["aya","ye","woo","ma"]
    for i in babbling:
        if "ayaaya" in i or "yeye" in i or "woowoo" in i or "mama" in i:
            continue
        for j in check:
            i=i.replace(j,"1")
        check_1=0
        for k in i:
            if k!="1":
                check_1=1
        if check_1!=1:
            answer+=1
        
    return answer