def solution(dartResult):
    previous = 0
    now = ""
    now_value = 0
    answer = 0
    for i in range(len(dartResult)):
        if now == "" or (now and now[-1].isalpha() and dartResult[i].isdigit()):
            now = ""
            now += dartResult[i]
            answer += previous
            previous = now_value
            now_value = 0
        elif now and now[-1].isdigit() and dartResult[i].isdigit():
            now += dartResult[i]
        elif dartResult[i].isalpha():
            now += dartResult[i]
            if len(now) == 2:
                if now[1] == "S":
                    now_value = int(now[0])
                elif now[1] == "D":
                    now_value = int(now[0]) ** 2
                elif now[1] == "T":
                    now_value = int(now[0]) ** 3
            elif len(now) == 3: 
                if now[2] == "S":
                    now_value = int(now[0] + now[1])
                elif now[2] == "D":
                    now_value = int(now[0] + now[1]) ** 2
                elif now[2] == "T":
                    now_value = int(now[0] + now[1]) ** 3
                
        elif dartResult[i] == "*":
            previous *= 2
            now_value *= 2
        elif dartResult[i] == "#":
            now_value *= -1
    return answer + now_value + previous
            
                