def solution(myString, pat):
    answer = ''
    for i in range(len(myString)):
        if myString[i]=='A':
            answer=answer+'B'
        elif myString[i]=='B':
            answer=answer+'A'
        else:
            answer+=myString[i]
    if pat in answer:
        return 1
    else:
        return 0