from collections import defaultdict
def solution(nums):
    n = len(nums)
    answer = 0
    num_dic = defaultdict(str)
    for num in nums:
        if num_dic[num] != 'True':
            answer += 1
        num_dic[num] = 'True'
    return min(answer, n // 2) 