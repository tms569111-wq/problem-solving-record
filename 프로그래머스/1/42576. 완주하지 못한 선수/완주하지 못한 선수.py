from collections import defaultdict
def solution(participant, completion):
    participant_dic = defaultdict(int)
    completion_dic = defaultdict(int)
    for i in range(len(participant) - 1):
        participant_dic[participant[i]] += 1
        completion_dic[completion[i]] += 1
    participant_dic[participant[-1]] += 1
    
    for key, value in participant_dic.items():
        if completion_dic[key] != value:
            return key
    