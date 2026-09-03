def solution(numbers, target):
    answer = [0]
    i = len(numbers)
    def dfs(now, idx):
        if idx == i:
            if now == target:
                answer[0] += 1
            return
        dfs(now + numbers[idx], idx + 1)
        dfs(now - numbers[idx], idx + 1)
        
    dfs(0, 0)
    return answer[0]