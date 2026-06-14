from itertools import combinations
from collections import Counter

def solution(orders, course):
    # 일단 hash dic
    # 각 조합을 넣을 필요가 있음
    # 영어 글자 1개씩만 세고...거기서 제일 큰 수 2개로 조합된 수를 2번, 그 다음을 3번 하면...?
    # 안 됨...예를 들어서 a가 100만 개 있고 wqertbsfq가 2번씩 있어도
    # 9개 코스는 a가 안 들어가고 wqertbsfq가 됨
    # 따라서 예를 들어서 abcfg는 abc, cfg, ..., 이런 식으로 조합을 해서 넣어야 함...
    # order가 20개 까지 들어오니까 10*9*8*7*6*5*4*3*2*1 최악의 경우 모든 조합하면 100만개 * 20 2000만번 연산...
    # 쓰읍...되려나???
    # 일단 해보자고
    answer=[]
    def dfs(order,size,idx,now,counter):
        if len(now)==size:
            menu=''.join(now)
            counter[menu]+=1
            return
        for i in range(idx, len(order)):
            now.append(order[i])
            dfs(order,size,i+1,now,counter)
            now.pop()
            
    for size in course:
        counter=Counter()
        for order in orders:
            order=sorted(order)
            dfs(order,size,0,[],counter)
        if not counter:
            continue
        max_count=max(counter.values())
        if max_count>=2:
            for menu,count in counter.items():
                if count==max_count:
                    answer.append(menu)
    return sorted(answer)