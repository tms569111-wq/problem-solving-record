from itertools import combinations
def solution(n, info):
    # 어피치의 점수를 보고 가장 큰 차이로 이기려면
    # 같은 건 불가능 점수 빼앗김
    # 가장 큰 점수부터 순서대로 이기는 게 좋지만...
    # 만약 어피치가 10에 10발 쏘고 라이언이 5발 있으면
    # 9, 8, 7, 6, 5 이렇게 넣으면 그만...
    # 그렇기 때문에 왠만한 방법으로는 알 수 없음
    # 그렇다고 완전탐색하기도 애매한 것이
    # 10발밖에 안 쏘기는 하지만
    # 10발을 11곳에 쏘는 경우의 수를 계산하면
    # 11 ^ 10
    # 1000000000
    # 거의 10억번...
    # 너무 연산해야할 횟수가 많음
    # 좀 가지치기 해야 하는 느낌
    # 일단, 어피치보다 작아질 것 같은 경우를 제외해야 함
    # 근데 어떻게 그런 경우를 제외하냐?
    # 상황 고려. 일단 어피치가 쏜 것들보다 적거나 같으면 걍 무의미함
    # 10발 맞 춘 곳에 같이 10발 맞춰도 짐
    # 그러니까 최선의 상황은 무조건 쏜 것들 보다 1개 더 많이 쏘거나
    # 아예 안 쏘는 경우
    # 그러면 계산이 좀 간단해질 듯
    # 와 여기까지 10분 넘게 고민했네 문제 어렵네 2레벨인데
    # 어피치 쏜 횟수를 다 고려할 수는 없음
    # 그러니까 아예 어피치가 쏜 거 안 건드리기 1개
    # 그 다음에는 어피치가 쏜 것들 1개씩만 건드린 것들 배열 n개
    # 2개씩만 건드린 것들 n * n-1
    # 3개씩, 4개씩, ..., n개씩 하면
    # 적어도 10억번은 안 할 수 있을 듯
    # 그 다음은 정렬
    # 일단 가장 큰 점수는 answer 배열과 같은 인덱스에 점수 배열을 만듦
    # 만약 가장 큰 점수가 현재 어피치 점수보다 적으면 탈락
    # 와 근데 이러면 현재 어피치 점수랑 라이언 점수 따로 구하고
    # 차이도 구해야 되네 개 귀찮네
    # 그 뒤 여기서 점수 값이 max인 것들만 따로 배열 만들고 
    # 그 뒤가 문제
    # 뒤에서 부터 비교해서 뒤에값 max인 놈들 따로
    # 그것도 같은 놈있으면 또 따로 해서 앞까지 쭉쭉쭉
    # 이게 시간복잡도가 될란가 몰라
    # 일단 손가락 움직임 ㄱㄱㄱ
    n = sum(info)
    candi_list = []
    def diff(num):
        ryan_list = [0] * 11
        for i in num:
            ryan_list[i] = info[i] + 1
        count = sum(ryan_list)
        if count > n:
            return
        for i in range(11):
            if ryan_list[i] == 0:
                if info[i] == 0:
                    if count == n:
                        continue
                    count += 1
                    ryan_list[i] = 1
            
            
        peach_score = 0
        score = 0
        for i in range(11):
            if info[i] != 0 and ryan_list[i] != 0:
                if ryan_list[i] > info[i]:
                    score += 10 - i
                else:
                    peach_score += 10 - i
            elif info[i] == 0 and ryan_list[i] != 0:
                score += 10 -i
            elif info[i] != 0 and ryan_list[i] == 0:
                peach_score += 10 - i
    
        if score > peach_score:      
            if sum(ryan_list) < n:
                ryan_list[10] += n - sum(ryan_list)
            candi_list.append((ryan_list, score - peach_score))
        else:
            return
        
    peach_idx = []
    for i in range(len(info)):
        if info[i] != 0:
            peach_idx.append(i)
    for i in range(len(peach_idx)):
        for num in combinations(peach_idx, i):
            diff(num)
    if candi_list == []:
        return [-1]
    candi_list.sort(key = lambda x:(-x[1], tuple(-x[0][i] for i in range(10, -1, -1))))
    max_num = candi_list[0][1]
    new_max = []
    for i in range(len(candi_list)):
        if candi_list[i][1] == max_num:
            new_max.append(candi_list[i])
    
    return candi_list[0][0]