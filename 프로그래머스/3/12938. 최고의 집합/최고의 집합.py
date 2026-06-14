def solution(n, s):
    # 일단 자연수인 게 힌트인듯???
    # 일단 자연수는 서로 곱해서 가장 커지려면 비슷한 숫자여야 함. 1,8, 2,7 보단 4,5처럼
    # s를 자연수 n개로 표현이니까 s/n을 하고 이걸 n만큼 for문으로 하면 될 듯?
    # s가 홀수면 중복이 안 되고 짝수면 중복
    # 123428193476 같은 수가 있다고 해보자...
    # 이걸 2로 나누면 이게 가능하지만
    # 나머지 차이가 많은 애들은...
    # 12342415 *n+12342보다
    # 12342444 *n 같은 게 더 크다.
    # 즉...일단 a를 구하고...
    # b를 a에다가 더하고 -n씩 뺀다...
    a=int(s//n)
    answer = []
    b=s%n
    for i in range(n):
        answer.append(a)
    check=len(answer)-1
    while b!=0:
        if check==-1:
            check=len(answer)-1
        answer[check]+=1
        b-=1
        check-=1
    if 0 in answer:
        return [-1]
    return answer