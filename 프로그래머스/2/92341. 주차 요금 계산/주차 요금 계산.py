import math
from collections import defaultdict
def solution(fees, records):
    in_time = defaultdict(int)
    total_time = defaultdict(int)

    for i in range(len(records)):
        time, number, IN_OUT = records[i].split(" ")
        h, m = time.split(":")
        minutes = int(h) * 60 + int(m)
        if IN_OUT == "IN":
            in_time[number] = minutes
        else:
            total_time[number] += minutes - in_time[number]
            in_time[number] = -1
    result = []
    last = 23 * 60 + 59
    for key, value in in_time.items():
        if value == -1:
            continue
        total_time[key] += last - value
    for key, value in total_time.items():
        if value <= fees[0]:
            result.append([key, fees[1]])
        elif value > fees[0]:
            value -= fees[0]
            result.append([key, fees[1] + math.ceil((value / fees[2])) * fees[3]])
    result.sort(key = lambda x : x[0])
    answer = []
    for i in result:
        answer.append(i[1])
    return answer
        
   