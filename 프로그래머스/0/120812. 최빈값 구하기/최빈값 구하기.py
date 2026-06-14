def solution(array):
    most_freq=[]
    most_count=[]
    index=0
    check=0
    for i in range(len(array)):
        if(array[i] not in most_freq):
            most_freq.append(array[i])
            most_count.append(1)
        else:
            index = most_freq.index(array[i])
            most_count[index]+=1
    most_count_value=max(most_count)
    for i in range(len(most_count)):
        if most_count_value==most_count[i]:
            index_last=i
            check=check+1
    if check!=1:
        return -1
    else:
        return most_freq[index_last]
        
        
    answer = 0
    return answer