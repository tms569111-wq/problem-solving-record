def solution(seoul):
    for i in range(len(seoul)):
        if 'Kim' in seoul[i]:
            return '김서방은 '+str(i)+'에 있다'
    answer = ''
    return answer