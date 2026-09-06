from collections import defaultdict
def solution(clothes):
    dic = defaultdict(lambda : 1)
    for i in range(len(clothes)):
        dic[clothes[i][1]] += 1
    count = 1
    for value in dic.values():
        count *= value
    return count - 1