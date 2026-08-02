import math
def solution(progresses, speeds):
    done_progress_list = []
    answer = []
    max_day = 0
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        if max_day == 0:
            max_day = day
        if done_progress_list != [] and max_day != 0 and max_day < day:
            answer.append(len(done_progress_list))
            
            max_day = day
            done_progress_list = []
        done_progress_list.append(day)
        
    
    answer.append(len(done_progress_list))
    return answer