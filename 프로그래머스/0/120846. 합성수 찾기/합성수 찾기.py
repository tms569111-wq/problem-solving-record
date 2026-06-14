def solution(n):
    count=0
    for i in range(1,n+1):
        count_2=0
        for j in range(1, i+1):
            if i%j==0:
                count_2+=1
        if count_2>=3:
            count+=1
    answer = count
    return answer