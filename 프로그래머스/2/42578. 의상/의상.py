from collections import defaultdict
from itertools import combinations
def solution(clothes):
    clothes_dic = defaultdict(int)
    for i in range(len(clothes)):
        clothes_dic[clothes[i][1]] += 1
    answer = 1
    for i in clothes_dic.values():
        answer *= (i + 1)
        
    return answer - 1