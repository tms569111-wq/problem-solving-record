from collections import deque
def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    while people:
        if len(people) == 1:
            answer += 1
            return answer
        if people[-1] + people[0] > limit:
            people.pop()
        else:
            people.pop()
            people.popleft()
        answer += 1
    return answer
    