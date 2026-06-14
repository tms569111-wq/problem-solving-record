def solution(gems):
    left=0
    gem_count={}
    total_kind=len(set(gems))
    answer=[1,len(gems)]
    min_len=len(gems)
    for right in range(len(gems)):
        gem=gems[right]
        gem_count[gem]=gem_count.get(gem,0)+1
        while len(gem_count)==total_kind:
            cur_len=right-left
            if cur_len<min_len:
                min_len=cur_len
                answer=[left+1,right+1]
            left_gem=gems[left]
            gem_count[left_gem]-=1
            if gem_count[left_gem]==0:
                del gem_count[left_gem]
            left+=1
    return answer