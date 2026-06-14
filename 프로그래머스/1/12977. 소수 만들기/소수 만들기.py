import math
def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return 0

    return 1

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                z=nums[i]+nums[j]+nums[k]
                answer+=is_prime_num(z)

    return answer