from collections import deque
def solution(queue1,queue2):
    # 두 큐 전체 합을 구한다.
    # 전체 합이 홀 수면 두 큐의 합을 같게 만들 수 없다.
    sum_all=sum(queue1)+sum(queue2)
    if sum_all%2==1:
        return -1
    # 각 큐가 목표로 해야 하는 합이다.
    # 전체 합의 절반이 되어야 한다.
    target=sum_all//2
    # queue1의 현재 합만 계속 관리 한다.
    # queue2의 합은 total-sum1이므로 따로 관리할 필요 없다.
    q1_sum=sum(queue1)
    
    # 작업 횟수다
    check=0
    queue1=deque(queue1)
    queue2=deque(queue2)
    
    # 무한 루프를 막기 위한 최대 작업 횟수다.
    # 각 원소가 여러 번 이동해도 이정도 안에 안 되면 불가능으로 본다.
    limit=len(queue1)*5
    while check<=limit:
        # queue1의 합이 목표 값이면 두 큐의 합이 같다는 뜻이다.
        if q1_sum==target:
            return check
        # queue1의 합이 목표보다 크면 queue1에서 하나 빼서 queue2로 보냄
        elif q1_sum>target:
            a=queue1.popleft()
            q1_sum-=a
            queue2.append(a)
            check+=1
            # queue1의 합이 목표보다 작으면 queue2에서 하나 빼서 queue1로 가져온다.
        elif q1_sum<target:
            a=queue2.popleft()
            q1_sum+=a
            queue1.append(a)
            check+=1
    return -1