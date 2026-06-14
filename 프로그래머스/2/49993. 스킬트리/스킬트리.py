def solution(skill, skill_trees):
    # 스택느낌적인 느낌
    # 큐도 쓸 까...
    answer =0
    for i in skill_trees:
        now_stack=0
        check=0
        for j in i:
            if j not in skill:
                continue
            else:
                if skill[now_stack]==j:
                    now_stack+=1
                elif skill[now_stack]!=j:
                    check=1
                    break
        if check==0:
            answer+=1
    
    return answer