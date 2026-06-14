def solution(s1, s2):
    count=0
    for i in s1:
        for j in s2:
            if i==j:
                count=count+1
                break;

    return count