import sys
sys.setrecursionlimit(3000000)
#계산 계산을 하자
# 일단 n은 14
# 빠르게 dfs?
# 시작은 무조건 (로 시작하고
# 끝은 )로 시작한다.
# 그러면 일단 1쌍은 빼고
# 쌍이 13쌍
# 26개
# 2^26은?
# 4^ 13 = 16 ^ 6 * 4 = 256 ^ 3 * 4= 50000 *1000
# 5천만
# 할만 하네?
# 걍 dfs ㄱㄱㄱ
# 문제는 리스트다.
# 리스트가 5천만개 들어가면 에바 세바
def solution(n):
    answer = [0]
    last_n = n * 2
    
    def dfs(now, now_n, now_left, now_right):
        if now_left < now_right:
            return
        if now_left > n:
            return
        if now_right > n:
            return
        
        if now_n == last_n - 1:
            if now_left == n and now_right + 1 == n:
                answer[0] += 1
            return
        else:
            
            stack_right = now.copy()
            
            stack_right.append(')')
            
            dfs(stack_right, now_n + 1, now_left, now_right + 1)
            
            stack_right[-1] = '('
            dfs(stack_right, now_n + 1, now_left + 1, now_right)
    stack =['(']
    dfs(stack, 1, 1, 0)
    return answer[0]