def solution(lottos, win_nums):
    # 로또 윈 넘버에서 같은 것들 체크
    count=0
    win_count=0
    for i in lottos:
        if i==0:
            count+=1
        elif i in win_nums:
            win_count+=1
    if win_count==0:
        if count==0 or count==1:
            return [6,6]
        else:
            return [7-count,6]
    else:
        answer = [7-win_count-count,7-win_count]
    return answer