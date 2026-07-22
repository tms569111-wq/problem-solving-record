# 작업이 n개
# cores마다 1개씩 배분
# 제일 빠른 코어는 일을 끝내고 새거를 받음
# 그런데 새거를 받고 다음 코어가 받을 수도 있고 다음 코어보다 제일 빠른 코어가 더 빨리 끝나서 걔가 더 할 수도 있음
# 이건 애매함.
# 내 생각에는 누적합 느낌
# 시간복잡도를 고려해보면 처리해야 하는 일이 5만개 안 넘는 다니까
# 5만을 n으로 나누고 그 숫자만큼 누적합을 둠
# 얘를 들어서 5만인데 n이 5다? 그럼 1만번 연산
# 맨 처음 걸 1시간부터 1만 시간까지
# 두 번째건 2시간 부터 2만 까지
# 아 이건 아닌가
# 그냥 5만까지 해?
# 코어의 수가 1만이고 일의 개수가 5만이면
# 5억번 연산?
# 시간이 애매 하다
# 일단 해보고 시간을 줄일 방법을 찾아볼까?
# 누적합 쓰면 될 것 같기도 하고
# 하다가 n보다 커지면 멈추는 걸로
def solution(n, cores):
    core_count = len(cores)
    if n<= core_count:
        return n
    
    left = 1
    right = min(cores) * n
    
    while left < right:
        mid = (left + right) // 2
        assigned_until_mid = core_count
        for core_time in cores:
            assigned_until_mid += mid // core_time
        if assigned_until_mid >= n:
            right = mid
        else:
            left = mid + 1
    target_time = left
    assigned_before = core_count
    for core_time in cores:
        assigned_before += (target_time - 1) // core_time
    for core_index, core_time in enumerate(cores):
        if target_time % core_time == 0:
            assigned_before += 1
            if assigned_before == n:
                return core_index + 1
        