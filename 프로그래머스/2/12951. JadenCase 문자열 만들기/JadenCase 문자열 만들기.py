def solution(s):
    answer = ""
    check = 0
    for string in s:
        if string == " ":
                answer += " "
                check = 0
        elif check == 0:
            if string.isdigit():
                answer += string
                check = 1
            else:
                answer += string.upper()
                check = 1
        else:
            answer += string.lower()
    return answer                
            
                
            
        