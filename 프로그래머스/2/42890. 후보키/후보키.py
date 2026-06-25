from itertools import combinations
def solution(relation):
    # 이거 애매하네
    # 일단 유일성은 각 열을 처음부터 끝까지 싸그리 싹싹 다 돌려보면서 같은 녀석이 나오면
    # 즉 set에 전부 넣은 것이랑 len이랑 다르면 바로 구별가능
    # 근데 최소성은? 
    # 이거 permutation한 뒤에 다음에 오는 값이 다 다르면 그만이긴 한데
    # 아 이거 모르겠다. db를 완벽히 알아야 이해가 되겠는데
    # 나 알긴아는데 슈퍼키는 유일성은 만족하지만 최소성 만족 안 함
    # 이 최소성이란 게 졸라 애매하네. 이름, 전공, 학년, 이름, 학년, 이름 학번
    # 이런 조합 다 permutation으로 구해도 어떻게 최소성만 구하지?
    # 모르곘다.
    
    #먼저 1개
    row = len(relation)
    col = len(relation[0])
    
    candidate_keys = []
    for size in range(1, col + 1):
        for cols in combinations(range(col), size):
            is_minimal = True
            for key in candidate_keys:
                if set(key).issubset(set(cols)):
                    is_minimal = False
                    break
            if not is_minimal:
                continue
            values = set()
            
            for r in range(row):
                temp = []
                for c in cols:
                    temp.append(relation[r][c])
                values.add(tuple(temp))
            if len(values) == row:
                candidate_keys.append(cols)
    return len(candidate_keys)