# 일단 10만 * 10만 하면 망함
# 길이로? 해쉬를 한 다면...
# 아니면 트라이 구조 쓰는 건가...?
# 트라이 제대로 안 배워서 잘 모르는데...
# 일단 words를 길이별로 나눈다...
# 길이가 같은 쿼리를 꺼낸다...
# 앞부터 비교...\
# 아 근데 전부 길이가 100만인 것들 10만개 이면...
# 10만 * 10만 * 100만인데...?
# 부분 점수라도 받아야지...
from collections import defaultdict
from bisect import bisect_left, bisect_right
def solution(words, queries):
    length_words = defaultdict(list)
    reverse_words = defaultdict(list)
    answer = []
    for word in words:
        n = len(word)
        length_words[n].append(word)
        reverse_words[n].append(word[::-1])
    for n in length_words:
        length_words[n].sort()
        reverse_words[n].sort()
    
    for query in queries:
        n = len(query)
        if n not in length_words:
            answer.append(0)
            continue
        if query[0] != '?':
            target_words = length_words[n]
            left_query = query.replace('?', 'a')
            right_query = query.replace('?', 'z')
        else:
            target_words = reverse_words[n]
            reversed_query = query[::-1]
            left_query = reversed_query.replace('?', 'a')
            right_query = reversed_query.replace('?', 'z')
        left = bisect_left(target_words, left_query)
        right = bisect_right(target_words, right_query)
        answer.append(right - left)
    return answer
    
    
    