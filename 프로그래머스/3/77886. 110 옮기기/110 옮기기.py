def solution(s):
    # 코테를 하면서 느낀점
    # 항상 역순으로 생각하라
    # 110을 모조리 찾아서 앞으로나 두번째로 넣는 것을 다 계산 하기도 있고
    # 이미 완성된 무언가가 있다고 가정한 뒤 그걸 바꿔서 s로 만들 수 있는지 계산할 수도 있다.
    # 일단 사전순이면 0이 더 앞으로 가야 됨
    # 즉 1111111111111111111111111111110이런식으로 1이 연속으로 있으면 안 됨
    # 보면 110은 1이 연속으로 있는 곳 맨 앞에 올 수 있음
    # 그리고? 110의 맨 앞에도 올 수 있음
    # 그런데? 0에 앞에는 못 있음
    # 그리고? 010 즉 10의 앞에도 못 있음
    # 결국 중요한 건 맨 앞임
    # 맨 앞을 보고 0이면 넘김
    # 1이면 뒤를 봄
    # 10이면 넘김
    # 11이면 110이나 111이나 둘다 앞
    # 즉 맨 앞이 11이 되는 순간을 구하고 11이면 11의 맨 앞 부분에 110을 넣으면 됨
    # 즉 모든 110을 구한 뒤에
    # 걔네를 다 지움
    # 이때 문자열이라 그냥 빼버리면 어려움
    # 위치만 구하고 슬라이싱 하면 n*2넘게 되니까
    # 걍 새로 s를 만들고 앞에서 부터 더하면 될 듯
    # 생각보다 간단한데? 해보자고
    # 와 근데 난 O(s)라 생각했는데 최악의 경우 O(s^2)네?
    # 뭐 log(n)방법이 있나?
    # 일단 해보자고
    
    new_s = ''
    answer = []
    stack = []
    for i in range(len(s)):
        count_110 = 0
        for j in range(len(s[i])):
            if s[i][j] == '1':
                stack.append('1')
            elif s[i][j] == '0':
                stack.append('0')
            while len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                
                count_110 += 1
                stack.pop()
                stack.pop()
                stack.pop()
        check_0 = ''
        n = len(stack)
        check_idx = n
        for i in range(len(stack)):
            if stack[i] == '0':
                check_0 = ''
                check_idx = n
                continue
            elif stack[i] == '1':
                check_0 += '1'
                check_idx = i
                if check_0 == '11':
                    check_idx = i - 1
                    break
        
        new_s = "".join(stack[0:check_idx]) + '110' * count_110 + "".join(stack[check_idx:])
        answer.append(new_s)
        stack = []
    
    return answer