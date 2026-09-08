from collections import defaultdict
def solution(s):
    dic = defaultdict(set)
    s = s[2:-2]
    now = list(s.split('},{'))
    for i in range(len(now)):
        split = set(now[i].split(","))
        length = len(split)
        dic[length] = split
    answer = []
    for i in range(1, len(now) + 1):
        answer.append(int(list(dic[i] - dic[i-1])[0]))
    return answer