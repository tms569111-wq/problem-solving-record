# 일단 어떤 부분집합으로 cookie배열을 잘라야 함
# 이때 나올 수 있는 조합은 너무 많음
# cookie 첫번째를 차지하면 뒤에 것들 다 어떻게 차지 하지? 
# n -1 ~ 1까지 조합을 해야 하는데 그럼 2000을 조합
# 즉 완전탐색으로는 도저히 구할 수 없음
# 이긴 하나? 조건이 같아야 되는데 1이상이기 때문에
# 이상인 것들은 체크 하지 않을 수는 있지만?
# 또 그렇다고 바구나의 과자수가 무조건 오름차순은 아니기 때문에
# 쉽지 않음
# dp를 해야 하나?
# 아니면 sum으로 전체 값을 구한 뒤 반으로 쪼개지는 지점을 찾아볼까
# 일단 길이가 2000이고 원소 값이 500이니까 10만번 연산인가?
# 일단은 시간복잡도 적긴 하네
# 이거 아니면 누적합? 
# 생각해보자. 먼저 홀수는 누적합 해도 안 되고 
# 제일 큰 짝수 기준
# 맨 처음부터 짝수의 절반을 넘어갈 때까지 하고
# 그 위치에서 왼쪽으로 한 칸씩 빼본다
# 그 값이 짝 수 절반보다 적으면 어차피 안 됨
# 오 이거 좋네
# 아닌가 이거 완전탐색으로 되나?
# 일단 해보자
def solution(cookie):
    answer = 0
    n = len(cookie)
    for mid in range(n - 1):
        l = mid
        r = mid + 1
        left = cookie[l]
        right = cookie[r]
        
        
        while True:
            if left == right:
                answer = max(left, answer)
            
            if left <= right and l > 0:
                l = l - 1
                left += cookie[l]
            elif right <= left and r < n - 1:
                r = r + 1
                right += cookie[r]
            else:
                break

    return answer