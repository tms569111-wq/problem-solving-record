def solution(numbers):
    arr = []
    for i in numbers:
        arr.append(str(i))
    arr.sort(key=lambda x: x * 4, reverse=True)

    answer = ''

    for i in arr:
        answer += i

    if answer[0] == '0':
        return '0'

    return answer