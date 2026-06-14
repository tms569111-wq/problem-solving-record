def solution(numbers, target):
    def dfs(index, sum_num):
        if index==len(numbers):
            return 1 if sum_num==target else 0
        return dfs(index+1,numbers[index]+sum_num)+dfs(index+1,sum_num-numbers[index])
    return dfs(0,0)