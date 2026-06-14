def solution(n, m, section):
    answer = 0
    last_painted = 0  
    
    for s in section:
        if s > last_painted:
            answer += 1
            last_painted = s + m - 1
            
    return answer