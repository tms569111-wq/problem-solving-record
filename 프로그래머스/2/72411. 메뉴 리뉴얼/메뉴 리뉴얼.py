from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    dic = defaultdict(int)
    new_dic = defaultdict(int)
    new_dic_real = defaultdict(list)
    for i in range(len(orders)):
        for j in range(len(course)):
            for k in combinations(orders[i], course[j]):
                k = list(k)
                k.sort()
                a = "".join(k)
                dic[a] +=1
                
    for key, value in dic.items():
        length = len(key)
        if length in course:
            if value >= 2:
                if new_dic[length] < value:
                    new_dic[length] = value
                    new_dic_real[length] = []
                    new_dic_real[length].append(key)
                elif new_dic[length] == value:
                    new_dic_real[length].append(key)
    answer = []
    for i in new_dic_real.values():
        for j in i:
            answer.append(j)
    answer.sort()
    return answer
        
        