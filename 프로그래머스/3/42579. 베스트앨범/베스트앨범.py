def solution(genres, plays):
    # 장르에 따라서 먼저 딕셔너리로 나눔
    # 같은 장르에서 크기 순으로 넣는 리스트를 만듬 리스트 [['classic',[(1,100) ]]...]
    # 3 dic로 품
    # 고유번호:크기 
    # 장르: 고유번호 얘는 리스트로
    # 장르: 크기
    dic={}
    dic_uni={}
    dic_genum=[[] for _ in range(100)]
    dic_ge=[]
    for i in range(len(plays)):
        if genres[i] not in dic_ge:
            dic_ge.append(genres[i])
        dic_genum[dic_ge.index(genres[i])].append(i)
        dic_uni[i]=plays[i]
        if genres[i] in dic:
            a=0
            a=dic[genres[i]]
            dic[genres[i]]=a+plays[i]
        else:
            dic[genres[i]]=plays[i]
    dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    answer=[]
    for i in range(len(dic)):
        print(dic[i][0])
        k=dic_ge.index(dic[i][0])
        q=len(dic_genum[k])
        print(k,q)
        big_1=0
        big_2=0
        b_1=0
        b_2=0
        for w in range(q):
            if big_2<dic_uni[dic_genum[k][w]]:
                big_2=dic_uni[dic_genum[k][w]]
                b_2=dic_genum[k][w]
            if big_2>big_1:
                big_1, big_2=big_2,big_1
                b_1,b_2=b_2,b_1
            if big_2==dic_uni[dic_genum[k][w]]:
                if dic_genum[k][w]<b_2:
                    b_2=dic_genum[k][w]
        if big_2!=0:
            answer.append(b_1)
            answer.append(b_2)
        else:
            answer.append(b_1)
    
    return answer