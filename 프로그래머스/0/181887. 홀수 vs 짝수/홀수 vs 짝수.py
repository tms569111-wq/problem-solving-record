def solution(num_list):
    count_1=0
    count_2=0
    for i in range(len(num_list)):
        if i%2==0:
            count_1+=num_list[i]
        else:
            count_2+=num_list[i]
    answer=max(count_1,count_2)
    return answer