def solution(people, limit):
    people.sort()
    check=0
    left=0
    right=len(people)-1
    answer=0
    while left<=right:
        if limit>=people[left]+people[right]:
            answer+=1
            left+=1
            right-=1
        else:
            right-=1
            answer+=1
        
    return answer