from functools import lru_cache
# a와 b중 선택해서 둘다 n과 m이 안 되는 선에서 a가 최소야 된다
# 일단 전부다 완전탐색하는 것은 불가능하다. 2^40은 어마어마한 숫자다
# dp를 쓰는 것도 애매한 게 값이 dp 할 때 똑같이 1을 넣는 게 아니라 1~3 사이 값을 넣기 때문
# 그러면 그리디를 하면 되는가? 하지만...둘 중 더 작은 걸 선택한다고 할 때에
# 모두 B가 선택하고 A가 선택 안 하는 경우도 있는데 몇몇 경우에 A가 더 작다는 이유 만으로
# A를 선택해야 될 수도 있다.
# 그러므로 정렬로 해결해보자
# 맨 처음 거를 B가 최소고 A가 최대인 경우로 정렬 몽땅 한 뒤에
# B가 다 먹고 죽게 되면 A가 작은 걸 먹는다면?
# 아닌가 걍 dp로 하는 게 맞나
# 이게 어렵네 은근. B가 3 3 3 3 3 3  3 2 2 2 2 1 1 1 1 1 1 1 1 1
#                 A가 1 1 1 1   1   1 1 1 1 1 1 1 1 1 1 2 2 2
# 이거 보니까 걍 B최대 A 최대로 B 먼저 채우고 그 뒤 A 하는 게 맞는 것 같긴 한데
# 아니다 걍 A가 최대가 되는 경우인데 b가 최소인 경우 b를 먼저 하는 게 맞겠지
def solution(info, n, m):
    info.sort(key = lambda x:(-x[0], x[1]))
    now_A = 0
    now_B = 0
    answer = [float('inf')]
    n_i = len(info)
    i = 0
    
    @lru_cache(None)
    def dfs(i, now_A, now_B):
        if i == n_i:
            answer[0] = min(answer[0], now_A)
            return
        
        if now_B + info[i][1] < m:
            dfs(i + 1, now_A,  now_B + info[i][1])
            
        if now_A + info[i][0] < n:
            dfs(i + 1, now_A  + info[i][0],  now_B)
        
        if now_A + info[i][0] >= n and now_B + info[i][1] >= m:
            return
        
    dfs(0, now_A, now_B)
    
    if answer[0] == float('inf'):
        return -1
    else:
        return answer[0]