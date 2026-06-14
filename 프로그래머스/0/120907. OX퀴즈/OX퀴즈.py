def solution(quiz):
    answer = []
    for i in quiz:
        a,op,b,eq,d=i.split()
        if op=='-':
            if int(d)!=(int(a)-int(b)):
                answer.append("X")
            else:
                answer.append("O")
        else:
            if int(d)!=(int(a)+int(b)):
                answer.append("X")
            else:
                answer.append("O")
    
    return answer