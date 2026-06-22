def solution(users, emoticons):
    # 어려워 보이는 군
    # 근데 완전탐색 하면 되는 느낌? 할인율은 40%~ 10%까지 4개인데 사람마다 할인이 다른 게 아니라 전체 이모티콘 7개에서 7^4니까
    # 아니다 4^7이구나 16 * 16 * 16 * 4 = 64 * 256 = 대충 10000개 
    # 완전탐색해도 100만개 정도 연산
    # 완전탐색이다
    # 가입자 수랑 값을 answer에 넣고 answer.sort(key = lambda x:x[0], x[1])하여서 answer[-1] 리턴하면 됨
    answer = []
    length = len(emoticons)
    combinations = []

    def all_dfs(previous, i):
        sale = [40, 30, 20, 10]
        if i == length:
            combinations.append(previous)
            return
        for sal in sale:
            new = []
            new = previous.copy()
            new.append([int(emoticons[i] * (100-sal)/100), sal])
            all_dfs(new, i + 1)
    
    all_dfs([], 0)
    for i in range(len(combinations)):
        money = 0
        plus_check = 0
        for j in range(len(users)):
            check = 0
            count = 0
            for k in range(len(combinations[0])):                
                if check == 0 and combinations[i][k][1] >= users[j][0]:
                    count += combinations[i][k][0]
                if count >= users[j][1]:
                    check = 1
                    count = 0
                    break
            money += count
            plus_check += check
        answer.append([plus_check, money])
    answer.sort(key = lambda x: (x[0], x[1])) 
    
    return answer[-1]
    
    