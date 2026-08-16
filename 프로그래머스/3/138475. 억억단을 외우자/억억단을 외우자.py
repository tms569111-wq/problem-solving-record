# 머리가 뜨끈해지는 문제로구나...
# 억억단? 즉 자연 수 곱하기 자연수...
# 자연수를 e보다 작은 범위에서 start[i]까지
# 숫자들 전부 1 * e부터 2 * (e//2) ~ ... (e root 2) * e root 2 ~   e * 1될 때까지
# 몇 번 나오나 구하면 되는데...
# 흠...일단 e가 5백만이고 e가 10만개이므로 
# 벌써 5천억... 이건 절 대 아님
# 그럼 미리 구해두면?
# 5백만 * 5백만이므로
# 이것도 훨씬 넘어버림
# 근데 사실 e root 2까지 하면 절반은 안 해도 되긴 한데
# 그래도 백만 * 백만을 넘어버림
# 심지어 그냥 값 만이 아니라 a 곱하기 b할 때 a랑 b도 세야 함.
# 뭐 감도 안 오네.;.....;;;
# 근데 저 표 그림 보면 살짝 감 오는 게 한 줄씩 보다보면
# 첫 줄은 1부터 1억 까지
# 둘 째 줄은 2부터 1억까지 2씩 증가
# 셋째 줄은 3부터 3억까지 n번 증가.
# 이런 식으로 반복하면
# i번째 줄은 i부터 1억까지 i번씩 증가함
# 그러면 for i in range(s, e + 1)
# 로 두고 첫째줄, 둘째줄 셋째줄을 각각 크기 구하면 됨
# 근데 이거 아무리 생각해도 시간 오바인데...
# dp 하기도 애매한 게 흠...e는 고정이어도 starts는 계속 변하는 제한 있고.
# 애매하네
from collections import defaultdict
def solution(e, starts):
    count = [0] * (e + 1)
    root = int(e ** 0.5)
    
    for d in range(1, root + 1):
        square = d * d
        count[square] += 1
        for num in range(square + d, e + 1, d):
            count[num] += 2
    best = [0] * (e + 1)
    best[e] = e
    for i in range(e - 1, 0, -1):
        if count[i] >= count[best[i + 1]]:
            best[i] = i
        else:
            best[i] = best[i + 1]
    return [best[s] for s in starts]
    
     
