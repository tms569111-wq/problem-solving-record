from collections import Counter

def solution(clothes):
    # 종류(category)만 다 모아서 개수를 센다
    counts = Counter([category for name, category in clothes])
    
    answer = 1
    for count in counts.values():
        answer *= (count + 1)
        
    return answer - 1