from collections import defaultdict
def solution(participant, completion):
    complete_person = defaultdict(int)
    answer = []
    for complete in completion:
        complete_person[complete] += 1
    for check in participant:
        if complete_person[check] == 0:
            return check
        if complete_person[check] != 0:
            complete_person[check] -= 1
        