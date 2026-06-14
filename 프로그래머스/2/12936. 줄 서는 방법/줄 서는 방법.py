import math
def solution(n, k):
    # 이거는 k를 1, 2,  3, 4,5 이런 숫자로 나눠보면서 할 수 있다.
    # 예를 들면 k는 5이기 때문에 n은 3이면 n은 3*2*1 해서
    # n은 6이다.
    # k-이때 n의 첫번째 원소가 들어갈 칸 * (n-1)
    # 그러면 2*2 이므로 k는 1이 된다.
    # 이걸 응용하면
    # k는 n 밑에서 나눠지기 1칸 전 원소부터 나누고 몫을 빼서 구하여야 하며
    # 몫은 n_list에서 1~20으로 구해야 한다.
    # 근데!!! 이거 21억을 넘는다
    # 그냥 넘는 것도 아니고 경단위!!!
    # 대황 파이썬 숭배합니다 그저 GOAT
    # 일단 작다고 생각해고 코드 짜보자
    
    n_list=[i for i in range(1,n+1)]
    answer=[]
    k-=1
    check=0
    for i in range(n,0,-1):
        fact=math.factorial(i-1)
        idx = k // fact
        answer.append(n_list.pop(idx))
        k%=fact
        
    return answer