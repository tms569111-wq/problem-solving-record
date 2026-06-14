def solution(num_list):
    z=1
    j=0
    for i in num_list:
        z=z*i
        j=j+i
    j=j*j
    if z<j:
        return 1
    else:
        return 0
