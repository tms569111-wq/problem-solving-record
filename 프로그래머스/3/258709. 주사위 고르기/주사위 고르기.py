# 최대 n이 10개
# 최악의 경우 5개 5개, 6^5 * 6^5 = 6^ 10 = 36 ^ 5 = 1296 ^ 2 * 36 = 5천만 정도
# 조합은 또 10 C 5니까 2 * 9* 8 * 7 * 6 = 42 120 = 약 4천 정도
# 총 연산 수 2000억 정도
# 즉 완전 탐색으로는 불가능하다...
# 그렇다면 추상적으로? 평균 기댓값이 더 높은 쪽이 이긴다고 하고, 평균 기댓값이 비슷하면
# 더 분산이 적은 쪽이 이기기 쉽다고 하면?
# 승리할 확률이니까 무랑 패랑 상관없이 승수만 높으면 되는데
# 아니면 뭐 기가막힌 dp로 빠르게 구할 수도 있나?
# 일단 평균 기댓값을 볼까. 1번은 21/6 2번은 20 / 6 3번은 19/ 6 4번은 20/ 6
# 흠 1번 고르는 건 그렇다 쳐도 2번과 4번은 같은 평균인데 왜 4번이 더 유리할까?
# 그건 1, 1과 5, 5과 각각 2번과 상충 되지만 4, 4가 1번 더 3을 이기기 때문...
# 오 그러면 그냥 평균으로 대소 관계 하고
# 평균 같은 애들끼리만 서로 대소 관계 각 원소당 뭐가 더 승률 높은지 비교하면 될 것 같은데
# 그런데! 평균이 높아도 또 1, 1, 1, 1, 1, 1000 이런 놈이면 확률상 또 애매하긴 해...
# 걍 전부 대소 비교 하면?
# 한 번 대소 비교시 6 * 6 = 36
# 다음 주사위 비교시 36 + 36
# 그 다음도 36 * 3 정도
# 오 기하급수 적이지는 않는다. 이러면 가능하지 함 해보자.
from itertools import combinations
from bisect import bisect_left
def solution(dice):
    n = len(dice)
    half = n // 2
    def make_sums(indices):
        sums = [0]
        for idx in indices:
            next_sums = []
            for current in sums:
                for value in dice[idx]:
                    next_sums.append(current + value)
            sums = next_sums
        return sums
    max_win = -1
    answer = []
    all_indices = set(range(n))
    for A in combinations(range(n), half):
        A = tuple(A)
        B = tuple(all_indices - set(A))
        A_sums = make_sums(A)
        B_sums = make_sums(B)
        B_sums.sort()
        win = 0
        for a in A_sums:
            win += bisect_left(B_sums, a)
        if win > max_win:
            max_win = win
            answer = [i + 1 for i in A]
    return answer