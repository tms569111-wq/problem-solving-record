def solution(sequence, k):
    left=0
    total=0
    min_len=len(sequence)
    answer=[0,len(sequence)-1]
    for right in range(len(sequence)):
        total+=sequence[right]
        while total>k:
            total-=sequence[left]
            left+=1
        if total==k:
            current_len=right-left
            if current_len<min_len:
                answer=[left,right]
                min_len=current_len
    return answer