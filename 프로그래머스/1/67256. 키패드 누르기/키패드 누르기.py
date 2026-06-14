def solution(numbers, hand):
    # 위치를 저장해야 해.
    # 눌러야 할 숫자가 중간에 있으면
    # 왼쪽 손 기준 중간 -1하고 길이 구하고
    # 오른쪽 손 기준 중간 +1 하고 길이 구함
    # *이랑 #은 각각 10과 12로 생각
    answer = ''
    right_now=12
    left_now=10
    left=[1,4,7,10]
    right=[3,6,9,12]
    for i in range(len(numbers)):
        if numbers[i]==0:
            numbers[i]=11
        if numbers[i]==right_now:
            answer+="R"
            continue
        if numbers[i]==left_now:
            answer+="L"
            continue
        print(left_now,right_now)
        if numbers[i] in left:
            answer+="L"
            left_now=numbers[i]
        elif numbers[i] in right:
            answer+="R"
            right_now=numbers[i]
        else:
            if left_now not in left:
                for_left=numbers[i]
                for_left=abs(for_left-left_now)-3
            else:
                for_left=numbers[i]-1
                for_left-=left_now
            if right_now not in right:
                for_right=numbers[i]
                for_right=abs(for_right-right_now)-3
            else:
                for_right=numbers[i]+1
                for_right-=right_now
            for_left=abs(for_left)
            for_right=abs(for_right)
            
            if for_left>for_right:
                right_now=numbers[i]
                answer+="R"
            elif for_left<for_right:
                left_now=numbers[i]
                answer+="L"
            else:
                if hand=="right":
                    right_now=numbers[i]
                    answer+="R"
                else:
                    left_now=numbers[i]
                    answer+="L"
    return answer