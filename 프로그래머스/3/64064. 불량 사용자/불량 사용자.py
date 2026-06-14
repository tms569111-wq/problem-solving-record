def solution(user_id, banned_id):
    # 수가 매우 작아서 완탐해도 될 듯 8^(4~5)정도?
    # 글자수가 같은 것 끼리 묶기.
    # list
    # 글자수가 같은 것들 중에서 *가 아닌 부위가 같은 것들만 살려두고 count++하면 될 듯
    # 와 ㅠㅠ 근데 *이 똑같은 경우도 있넹
    # 이러면 모든 경우의 수 구하고 같은 거 있으면 빼야 될 듯.
    ban_2_list=[]
    for ban in range(len(banned_id)):
        b=len(banned_id[ban])
        ban_list=[]
        for user in user_id:
            if len(user)==b:
                count=0
                for i in range(b):
                    if banned_id[ban][i]!="*":
                        if banned_id[ban][i]!=user[i]:
                            count=1
                            break
                if count==0:
                    ban_list.append(user)
        ban_2_list.append(ban_list)
    # dfs로 풀기
    result=set()
    use=[]
    def dfs(depth):
        if depth==len(banned_id):
            result.add(tuple(sorted(use)))
            return 
        for user in ban_2_list[depth]:
            if user in use:
                continue
            use.append(user)
            dfs(depth+1)
            use.pop()
    dfs(0)
    return len(result)
    
                        