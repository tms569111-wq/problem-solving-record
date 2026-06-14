from collections import Counter
def solution(N, stages):
    dic={}
    answer={}
    total_players=len(stages)
    dic=Counter(stages)
    for stage in range(1,N+1):
        if total_players>0:
            current_stage_players=dic[stage]
            answer[stage]=current_stage_players/total_players
            total_players-=current_stage_players
        else:
            answer[stage]=0
        
    
    answer=sorted(answer, key=lambda x: answer[x], reverse=True)
    return answer