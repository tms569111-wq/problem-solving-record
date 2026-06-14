from collections import Counter
def solution(X, Y):
    arr=[]
    x=Counter(X)
    y=Counter(Y)
    for i in range(9,-1,-1):
        char=str(i)
        common_count=min(x[char],y[char])
        arr.append(common_count*char)
    result="".join(arr)
    if result=='':
        return "-1"
    if result[0]=="0":
        return "0"
    # 카운터 9부터 공통 숫자만큼 뽑아서 더함
    return result