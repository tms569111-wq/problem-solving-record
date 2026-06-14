def solution(a, d, included):
    sum_1=0
    for i in range(len(included)):
        if included[i]==True:
            sum_1=sum_1+a+(d*i)
    return sum_1