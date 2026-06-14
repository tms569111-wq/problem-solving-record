from itertools import permutations

def solution(numbers):
    # 숫자 순열
    nums=set()
    for i in range(1, len(numbers)+1):
        for num in permutations(numbers,i):
            nums.add(int("".join(num)))
    # 에라토스테네스의 체
    max_num=max(nums)
    prime=[True]*(max_num+1)
    prime[0]=False
    prime[1]=False
    for idx in range(2, max_num+1):
        if prime[idx]:
            
            for j in range(idx*idx, max_num+1,idx):
                prime[j]=False
    # 소수 체크
    answer=0
    for number in nums:
        if prime[number]==True:
            answer+=1
    return answer