from math import gcd
def solution(arrayA, arrayB):
    # 길이랑 원소가 너무 큼...
    # 일단 arrayA의 숫자를 나누는 정수들 집합 구하고
    # 그것들 중의 arrayB를 못 나누는 정수들 집합 구하고
    # 반대도 구하고
    # 그것들 중의 제일 큰 거 구해야 하는데...
    # 에라토스테네스의 체? 근데 이건 소수 구하는 건데..
    # 감도 안 오네....
    answer = 0
    def g(a):
        result=a[0]
        for i in range(1,len(a)):
            result=gcd(result,a[i])
            if result==1:
                break
        return result
    ab=g(arrayA)
    ba=g(arrayB)
    def check(a,arr):
        if a==1:
            return False
        for i in arr:
            if i%a==0:
                return False
        return True
    
    answer=0
    if check(ab,arrayB)==True:
        answer=ab
    if check(ba,arrayA)==True:
        if ab<ba:
            answer=ba
    return answer