from collections import defaultdict
def solution(id_list, report, k):
    reported = defaultdict(int)
    repo = defaultdict(list)
    report = set(report)
    answer = [0 for _ in range(len(id_list))]
    for rep in report:
        reporter, bad = rep.split(" ")
        reported[bad] +=1
        repo[reporter].append(bad)
    count = 0
    for name in id_list:
        for n in repo[name]:
            if reported[n] >= k:
                answer[count] +=1
        count += 1
    return answer
   