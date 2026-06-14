def solution(survey, choices):
    # 일단 글자를 자른다.
    # 앞 글자를 int화 한다.
    # 해당 인트에 초이스 한 것을 구한다.
    # 나중에 지표 별 사전 순 정렬.
    ch_list=['R','T','C','F','J','M','A','N']
    ch_value=[0,0,0,0,0,0,0,0]
    for i in range(len(choices)):
        num=choices[i]
        num=num-4
        if num==0:
            continue
        elif num>0:
            ch=survey[i][1]
            idx=ch_list.index(ch)
            ch_value[idx]+=num
        else:
            ch=survey[i][0]
            idx=ch_list.index(ch)
            ch_value[idx]+=(num*-1)
    answer=""
    for i in range(0,len(ch_value),2):
        if ch_value[i]>=ch_value[i+1]:
            answer+=ch_list[i]
        elif ch_value[i]<ch_value[i+1]:
            answer+=ch_list[i+1]
    return answer