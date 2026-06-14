def solution(record):
    # 길이가 100000이상 최대 nlogn
    #일단 record를 split하고
    # enter면 result에 추가
    # leave면 result에 추가
    # change이면 uid로 바꿈.
    result=[]
    nick_name={}
    answer = []
    for red in record:
        ch=red[0]
        if ch=="L":
            a,b=red.split(" ")
            result.append([a,b])
        else:
            a,b,c=red.split(" ")
            nick_name[b]=c
            result.append([a,b])
    for i in range(len(result)):
        if result[i][0]=="Enter":
            answer.append(nick_name[result[i][1]]+"님이 들어왔습니다.")
        elif result[i][0]=="Leave":
            answer.append(nick_name[result[i][1]]+"님이 나갔습니다.")
            
    
            
            
    
    
    return answer