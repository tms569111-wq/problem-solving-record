import string
from collections import defaultdict
def solution(msg):
    dic = defaultdict(int)
    answer = []
    for i in range(len(string.ascii_uppercase)):
        dic[string.ascii_uppercase[i]] = i + 1
    now = ""
    count = 26
    for i in range(len(msg)):
        if dic[now + msg[i]] == 0:
            count += 1
            dic[now + msg[i]] = count
            answer.append(dic[now])
            now = msg[i]
        else:
            now = now + msg[i]
    answer.append(dic[now])
    return answer
            
    