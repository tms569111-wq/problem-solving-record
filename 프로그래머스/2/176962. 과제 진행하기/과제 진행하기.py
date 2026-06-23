def solution(plans):
    # stack으로 푸는 게 맞는 듯
    # 어렵지 않아보이고 딱히 함정도 없는 듯?
    
    def to_minute(time):
        h, m = time.split(":")
        return int(h) * 60 + int(m)
    
    plans = [[name, to_minute(start), int(playtime)] for name, start, playtime in plans]
    plans.sort(key = lambda x : x[1])
    
    answer = []
    stack = []
    
    for i in range(len(plans) - 1):
        name, start, playtime = plans[i]
        next_start = plans[i + 1][1]
        
        available = next_start - start
        
        if playtime <= available:
            answer.append(name)
            remain_time = available - playtime
            
            while stack and remain_time > 0:
                prev_name, prev_time = stack.pop()
                
                if prev_time <= remain_time:
                    answer.append(prev_name)
                    remain_time -= prev_time
                else:
                    stack.append([prev_name, prev_time - remain_time])
                    remain_time = 0
        else:
            stack.append([name, playtime - available])
    answer.append(plans[-1][0])
    
    while stack:
        answer.append(stack.pop()[0])
    return answer
    