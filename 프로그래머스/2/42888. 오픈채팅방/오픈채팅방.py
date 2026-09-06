from collections import defaultdict
def solution(record):
    uid = defaultdict(str)
    for i in record:
        if i[0] == 'C' or i[0] == 'E':  
            a, b, c = i.split(" ")
            uid[b] = c
    answer = []
    for i in record:
        if i[0] == 'E': 
            a, b, c = i.split(" ")
            answer.append(uid[b] + "님이 들어왔습니다.")
        elif i[0] == 'L': 
            a, b = i.split(" ")
            answer.append(uid[b] + "님이 나갔습니다.")
            
    return answer     
        
        
        
   