from collections import defaultdict
def solution(nums):
    dic = defaultdict(int)
    check = len(nums) // 2
    for i in nums:
        dic[i] +=1
    count = 0
    for key in dic.keys():
        count += 1
        if count >= check:
            return count
    return count