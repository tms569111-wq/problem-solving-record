def solution(strArr):
    check=[]
    check_num=[]
    for i in strArr:
        if len(i) not in check:
            check.append(len(i))
            check_num.append(1)
        else:
            z=0
            z=check.index(len(i))
            check_num[z]=check_num[z]+1
    answer = max(check_num)
    return answer