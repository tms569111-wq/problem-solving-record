import heapq
from collections import defaultdict
def solution(operations):
    # 이거 걍 최댓값 먼저 없애고 난 뒤 최소값 없애면 될 듯?
    # 아 씨 그건 안 되나?
    min_que = []
    max_que = []
    max_count = 0
    fix = []
    answer = []
    dic = defaultdict(int)
    for i in operations:
        if i[0] =='I':
            num = int(i[1:])
            heapq.heappush(min_que, num)
            heapq.heappush(max_que, -num)
            fix.append(num)
            dic[num] = 2
        elif i == "D 1":
            while max_que:
                num = -1 * heapq.heappop(max_que)
                if dic[num] != 2:
                    continue    
                else:
                    dic[num] -= 1
                    break
        else:
            while min_que:
                num = heapq.heappop(min_que)
                if dic[num] != 2:
                    continue    
                else:
                    dic[num] -= 1
                    break
    for num in fix:
        if dic[num] == 2:
            answer.append(num)
    if answer == []:
        return [0, 0]
    else:
        return [max(answer), min(answer)]
                
            
    
    