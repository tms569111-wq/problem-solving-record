def solution(answers):
    bun_1=[1,2,3,4,5]
    bun_2=[2,1,2,3,2,4,2,5]
    bun_3=[3,3,1,1,2,2,4,4,5,5]
    answer = []
    b_1=0
    b_2=0
    b_3=0
    for i in range(len(answers)):
        if answers[i]==bun_1[i%5]:
            b_1+=1
        if answers[i]==bun_2[i%8]:
            b_2+=1
        if answers[i]==bun_3[i%10]:
            b_3+=1
    a_0=[b_1,b_2,b_3]
    if b_1==b_2 and b_1==b_3:
        return [1,2,3]
    elif b_1==b_2 and b_1>b_3:
        return [1,2]
    elif b_3==b_2 and b_3>b_1:
        return [2,3]
    elif b_3==b_1 and b_1>b_2:
        return [1,3]
    elif max(a_0)==b_1:
        return [1]
    elif max(a_0)==b_2:
        return [2]
    elif max(a_0)==b_3:
        return [3]
    
    
