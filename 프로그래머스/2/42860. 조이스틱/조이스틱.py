def solution(name):
    # 9 + 1 + 13
    # 이거 묘하게 이해가 안 가네
    # 왼쪽으로 이동이나 오른쪽으로 이동한 다는 게 이동하면 아무것도 없는 무 상태가 아니라
    # A라는 소리 같은데
    # 흠 그러면 생각보다 간단한 거 아닌가?
    # 일단 다 AAAAA로 되어 있으니까
    # 만약 만들어야 할 게 JQWEAAAAAAAAAAAAAAAW 이런 거면
    # jqwe까지 갔다가 돌아가서 w하면 됨
    # 즉 알파벳 중간 기준 어디 가까운지로 위아래 결정
    # 전체 중 A조합이 가장 많은 곳이 그곳 까지 가는 곳보다 많으면 갔다 왔다. 아니면 그냥 오른쪽으로 가기
    # 아니면 처음부터 왼쪽으로 조이스틱 인지 대소 비교
    # 절반 기준 A가 qwadf이러면 그냥 오른쪽 쭉이랑 오른쪽 갔다 왼쪽이랑 같음
    # 절반 기준 a가 qwehrwgaaawwwwwwwwafasdgotwehtiuaaaaaaaaaw이러면?
    # w갔다가 다시 와서 오른쪽 쭉...
    # 이걸 씹 어캐하냐
    # 아예 완전 탐색을 해버려?
    # 계산 해보자.
    # 위 아래로 바꾸는 숫자는 정해져 있어
    # 좌우가 문제임
    # 왼쪽 쭉 가다가 돌아오는 경우
    # 한 칸 앞에 갔다가 뒤로
    # 전체 돌 때 까지 앞 뒤, 앞앞 뒤 뒤뒤 이런식으로 왔다리 갔다리 가능...
    # 2^20?아니야...
    # 그럴리는 없곘지만 거의 끝까지 가서 백도 가능하니까
    # 2^40정도...
    # 2^40이면 얼마지?
    # 암튼 에바임
    # 그러니까 조건을 걸어야됨
    # 만나는 놈이 a면
    # a를 감수하고 넘어가는 경우를 1번
    # a를 만나자마자 백도 하는 경우를 2번
    # 이걸 왼쪽으로 가서 시작하는 경우랑 
    # 오른쪽으로 가서 시작하는 경우를 한다
    # 이러면 확실히 숫자가 줄 듯
    # min으로 구하기
    answer = 0
    # 1. 일단 각 조이스틱 상하부터
    def up_down_check(char):
        if ord(char) < ord('N'):
            return ord(char) - ord('A')
        else:
            return 26 - (ord(char) - ord('A'))
    for char in name:
        answer += up_down_check(char)
    n = len(name)
    # 2. 조이스틱 좌우
    move = n - 1
    for i in range(n):
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        right_then_left = 2 * i + n - next_idx
        left_then_right = i + 2 *(n - next_idx)
        move = min(move, right_then_left, left_then_right)
    return answer + move