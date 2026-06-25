import copy
def solution(n):
    # 12개가 최대, 상하좌우 대각선을 12개씩 최대 36곳
    # 432 * 12니까
    # 4000번만 하면 되네? 엄청 널널널쓰 하군
    # 이 아니라 퀸의 위치가 정해져 있지 않아
    # 모든 퀸의 배치는 12*12 144중 선택하면
    # 144 * 143 * 142 ... 134까지
    # 100^10에다가 4000번???
    # 몇 천 경번보다 많다...
    # 즉 생각을 아예 바꿔야 함
    # 조건을 애초에 판을 둘 때 같은 줄에 안 두고
    # 같은 대각선에 안 둬야 한다는 제한을 걸면?
    # 가능한 배치 수가 확 줄 것 같은데
    # 일단 가능 배치 조합부터 구하자
    # 배치 조합을 dfs로 구하면 될 듯
    answer = 0
    cols = set()
    diag1 = set()
    diag2 = set()
    
    def dfs(row):
        nonlocal answer
        if row == n:
            answer += 1
            return
        for col in range(n):
            if col in cols:
                continue
            if row + col in diag1:
                continue
            if row - col in diag2:
                continue
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)
            
            dfs(row + 1)
            
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)
    dfs(0)
    return answer