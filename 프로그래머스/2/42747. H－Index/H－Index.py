# 최대 1000번
from collections import defaultdict
def solution(citations):
    length = len(citations)
    citations.sort()
    answer = 0
    dic = defaultdict(int)
    
    for i in range(length):
        if length - i <= citations[i]:
            dic[citations[i]] = length - i
    for value in dic.values():
        answer = max(answer, value)
    return answer