def solution(players, callings):
    rank={}
    
    for i,name in enumerate(players):
        rank[name]=i
        
    for name in callings:
        idx=rank[name]
        front=players[idx-1]
        players[idx-1],players[idx]=players[idx],players[idx-1]
        
        rank[name]-=1
        rank[front]+=1
        
    return players
    
    
    
    
    
    
    
    