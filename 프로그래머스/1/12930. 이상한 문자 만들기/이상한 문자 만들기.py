def solution(s):
    string = list((s.split(" ")))
    answer = ""
    for now in string:
        for i in range(len(now)):
            if i % 2 == 0:
                answer += now[i].upper()
            else:
                answer += now[i].lower()
        answer += " "
    return answer[0:-1]