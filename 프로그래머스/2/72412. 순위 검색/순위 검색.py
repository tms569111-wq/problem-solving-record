from collections import defaultdict
from bisect import bisect_left


def solution(info, query):
    # 5만 * 10만 해봤자 5억
    # 아니네 생각보다 크네
    # 흠...어떻게 할까?
    # 일단 맨 처음 info배열에서
    # 나누고
    # 거기서 뽑아 쓸까?
    # 아니 근데 쿼리 가능한 갯수가 4 * 3 * 3 * 3이잖아?
    # 12 * 9 = 108이면
    # 걍 info를 108개로 구분하고, 점수로 sort하면 되려나
    data = defaultdict(list)
    for person in info:
        arr = person.split()
        conditions = arr[:4]
        score = int(arr[4])
        for mask in range(16):
            key = []
            for i in range(4):
                if mask & (1<<i):
                    key.append('-')
                else:
                    key.append(conditions[i])
            data[tuple(key)].append(score)
    for key in data:
        data[key].sort()
    answer = []
    for q in query:
        q = q.replace(" and ", " ")
        arr = q.split()
        key = tuple(arr[:4])
        target_score = int(arr[4])
        scores = data[key]
        idx = bisect_left(scores, target_score)
        answer.append(len(scores) - idx)
    return answer