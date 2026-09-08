def solution(files):
    head_num = []
    answer = []
    for i in range(len(files)):
        phase = 0
        head = ""
        number = ""
        for j in range(len(files[i])):
            if phase == 0:
                if not files[i][j].isdigit():
                    head += files[i][j]
                else:
                    phase += 1
                    number += files[i][j]
            elif phase == 1:
                if not files[i][j].isdigit():
                    break
                else:
                    number += files[i][j]
            
        head_num.append((head.lower(), int(number), i))

    head_num.sort(key = lambda x : (x[0], x[1], x[2]))
    for i in range(len(head_num)):
        answer.append(files[head_num[i][2]])
    return answer
                
                    