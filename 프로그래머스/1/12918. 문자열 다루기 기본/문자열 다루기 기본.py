def solution(s):
    a=['1','2','3','4','5','6','7','8','9','0']
    for i in s:
        if i not in a:
            return False
    answer=False
    if len(s)==4 or len(s)==6:   
        answer = True
    return answer