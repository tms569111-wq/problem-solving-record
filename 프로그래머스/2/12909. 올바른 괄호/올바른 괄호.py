def solution(s):
    answer = True
    _1=0
    _2=0
    for i in s:
        if _2>_1:
            return False
        if i=='(':
            _1+=1
        else:
            _2+=1
    print(_1,_2)
    if s[0]==')':
        return False
    if _1==_2:
        return answer
    return False