# 일단 문자열들을 그냥 합치면 27^11정도라서 너무 큼
# 트라이 구조 같은데?
# 아니면 정렬해서 앞인지 뒤인지 찾고
# 그냥 앞에 있는 그 수만 빼나?
# 아 오히려 간단한가?
# 얘가 10개 문자열인데 'abcdesgf'
# 이런식이면 a는 첫번째니까 일단 26 ^ 7
# 그 다음은 26 ^ 6 에다가 2번째니까 * 2
# 이런 식으로 내려가면서 현재 위치 찾고
# 그 뒤 사전순으로 앞에 있는 거 제거
# 근데??? 그 뺀 게 또 밴일 수도 있음
# 흐음...밴도 길어서 not in으로 뺄 수도 없고
# 이거는 표시를 할까.
# ban을 해쉬에 넣고 사전순에서 빼되 해쉬 체크면 거르기
# 26진수 느낌으로 찾기
def solution(n, bans):
    def to_number(word):
        length = len(word)
        number = 0
        for l in range(1, length):
            number += 26 ** l
        value = 0
        for ch in word:
            value = value * 26 + (ord(ch) - ord('a'))
        return number + value + 1
    def to_word(number):
        length = 1
        while number > 26 ** length:
            number -= 26 ** length
            length += 1
        number -= 1
        result = ['a'] * length
        for i in range(length - 1, -1, -1):
            result[i] = chr(ord('a') ++ number % 26)
            number //= 26
        return ''.join(result)
    ban_numbers = []
    for ban in bans:
        ban_numbers.append(to_number(ban))
    ban_numbers.sort()
    target = n
    for ban in ban_numbers:
        if ban <= target:
            target += 1
        else:
            break
    return to_word(target)