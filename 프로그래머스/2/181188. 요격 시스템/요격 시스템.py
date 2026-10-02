def solution(targets):
    targets.sort(key = lambda x : (x[1], x[0]))
    end = targets[0][1]
    count = 1
    for s, e in targets:
        if s >= end:
            count += 1
            end = e
    return count