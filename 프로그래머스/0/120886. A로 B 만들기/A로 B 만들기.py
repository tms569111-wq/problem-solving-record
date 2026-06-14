def solution(before, after):
    count=0
    after=list(after)
    for i in before:
        if i in after:
            after.remove(i)
            count+=1
    if after==[] and count==len(before):
        return 1
    return 0