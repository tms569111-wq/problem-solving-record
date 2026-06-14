def solution(prices):
    n = len(prices)
    answer = [i for i in range(n - 1, -1, -1)]
    
    stack = []
    
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            past_index = stack.pop()
            answer[past_index] = i - past_index
        
        
        stack.append(i)
        
    return answer
