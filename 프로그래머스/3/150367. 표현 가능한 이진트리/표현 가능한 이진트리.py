# 헐 이거 감도 안 오네 핵어려워 보이네
# 일단 드는 생각은 숫자를 십진수를 이진 수로 바꾼다.
# 그 뒤 리프 노드라는 게 몇 개까지 생길 수 있는 가 계산
# 포화 이진 트리에서는 꽉꽉 채워야됨
# 0이든 1이든 일단 레벨에 따라서 다 구현할 수 있다
# 문제는 딱 하나!
# 루트 노드가 0이 되는 경우
# 5에 경우는 왼쪽 부터 볼 때에 101이어야 하는데 루트 노드가 0일 수 없으니까 탈락
# 95는 계산하기 복잡하지만 아마 0이 안 되서 그렇겠지
# 굳이 하자면 1011111인데
# 흠...왜 안 되나? 1이 7개 들어가는 군
# 즉 왼쪽부터 하자면 2가 루트 노드의 밑이니까 얘가 없으면 안 된다라
# 흠 굳이 구하자면 십진수를 일단 2진수로 만들고 
# 그 뒤 중간 놈이 0인 지 구하고
# 반 갈 죽 하고 반 가른 놈이 또 0인지 구하고
# 이거 반복하면 되려나?
# 10**15도 생각보다 len으로 치면 50정도네
# 50만이면 되긴 하는데
# 일종의 merge sort 라기보단 divide and conquer 느낌
# 근데 끝의 끝인 리프노드나 그런 건 없어도 되고
# 흠 체크 할 게 많네
# 일단 len 이 50이어도 무조건 50을 하는 게 아니라 중간 중간 추가를 해야 됨
# 그니까 크기에 맞는 포화 이진트리 레벨 이 있음
# 예를 들어서 레벨 0이면 1개 (0, 1 2^ 1 -1) 1이면 3개 ( 2, 3, 4, 5, 6, 7 즉 2^3 -1 ) 
# 레벨 2면 2^7 -1 이런 식인데
# 걍 2진수로 변환 해둔 상태니까
# 이진법 하는 노드 개수로 표현하자면 node = 1 이후 노드는 2*node + 1개 반복임
# 최대 len이 50 이므로 63개까지만 하면 됨
# 2의 63이 2의 50승 보다 더 크므로!
# 그러면 먼저 numbers가 오면 일단 대소 비교를 한 다
# bin으로 바꾸고 str로 만든 뒤 len이 level 어디 쯤에 있나 체크
# 그뒤 루트  맨 앞에 0을 포화이진트리 만큼 붙임
# def node_check로 맨 위 부터 반반씩 재귀함수로 내려감
# 만약 현재 위치가 str위치와 같게 할 때 부모가 0이면 return 0
# 맞으면 계속 감

def solution(numbers):
    class InvalidValueException(Exception):
        pass
    node = 1
    level = []
    answer = []
    for i in range(6):
        level.append(node)
        node = node * 2 + 1 
    
    
    def divide_and_conquer(bin_st, previous):
        middle = len(bin_st) // 2
        now = bin_st[middle]
        
        if previous == 'void' and now == '1':
            raise InvalidValueException()
        if len(bin_st) == 1:
            return
        if now == '0':
            next_previous = 'void'
        else:
            next_previous = 'exist'
        divide_and_conquer(bin_st[0:middle], next_previous)
        divide_and_conquer(bin_st[middle + 1:], next_previous)
    for num in numbers:
        binary = bin(num)[2:]
        bin_st = str(binary)
        n = len(bin_st)
        level_binary = 0
        complete = ''
        for i in range(5):
            if n == level[i]:
                level_binary = level[i]
                complete = bin_st
                break
            elif n >level[i]:
                if n <= level[i + 1]:
                    level_binary = level[i + 1]
                    tem = ''
                    for _ in range(level_binary - n):
                        tem += '0'
                    complete = tem + bin_st
                    break
        try:
            divide_and_conquer(complete, 'root')
            answer.append(1)
        except InvalidValueException as e:
            answer.append(0)
            continue
        
    
    return answer