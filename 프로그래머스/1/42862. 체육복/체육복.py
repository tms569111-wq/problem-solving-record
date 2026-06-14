def solution(n, lost, reserve):
    actual_reserve = sorted(list(set(reserve) - set(lost)))
    actual_lost = sorted(list(set(lost) - set(reserve)))
    
    for r in actual_reserve:
        if r - 1 in actual_lost:
            actual_lost.remove(r - 1)
        elif r + 1 in actual_lost:
            actual_lost.remove(r + 1)
            
    return n - len(actual_lost)
