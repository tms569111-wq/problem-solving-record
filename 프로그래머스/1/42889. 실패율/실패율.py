from collections import defaultdict
def solution(N, stages):
    dic = defaultdict(float)
    dic_num = defaultdict(int)
    stages.sort()
    n = len(stages)
    for i in range(n):
        dic_num[stages[i]] +=1
    for i in range(1, N + 1):
        if n == 0:
            dic[i] = 0
            continue
        dic[i] = dic_num[i] / n 
        n = n - dic_num[i]
    a = list(dic.items())
    
    a.sort(key = lambda x : (-x[1], x[0]))
    answer = [a[i][0] for i in range(len(a))]
    return answer
        
        
    
    