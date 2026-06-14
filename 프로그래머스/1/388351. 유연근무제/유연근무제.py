def solution(schedules, timelogs, startday):
    # 지금 날짜를 일단 구하는 것
    answer = 0
    
    for i in range(len(schedules)):
        limit=schedules[i]+10
        now_time=startday
        check=0
        if int(str(limit)[-2])>=6:
            limit+=100-60
        for j in timelogs[i]:
            if now_time>7:
                now_time-=7
            if now_time==7 or now_time==6:
                now_time+=1
                continue
            else:
                if limit<j:
                    check=1
                    break
            now_time+=1
        if check==0:
            answer+=1
    return answer