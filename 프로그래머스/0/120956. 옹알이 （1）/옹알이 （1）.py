def solution(babbling):
    count=0
    for i in babbling:
        i=i.replace("aya", " ")
        i=i.replace("woo", " ")
        i=i.replace("ye", " ")
        i=i.replace("ma", " ")
        if i.strip() == '':
            count=count+1
    answer = count
    return answer