from collections import Counter

def solution(nums):
    counts = Counter(nums) 
    type_count = len(counts)
    
    return min(len(nums) // 2, type_count)