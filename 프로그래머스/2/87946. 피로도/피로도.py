from itertools import permutations
def solution(k,dungeons):
    max_counts=0
    for p in permutations(dungeons):
        current_k=k
        count=0
        for min_s, sp in p:
            if current_k>=min_s:
                current_k-=sp
                count+=1
            else:
                break
        max_counts=max(count,max_counts)
    return max_counts