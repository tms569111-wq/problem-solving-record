def solution(elements):
    n=len(elements)
    extends=elements*2
    s=set()
    for i in range(n):
        current_sum=0
        for j in range(i,i+n):
            current_sum+=extends[j]
            s.add(current_sum)
    return len(s)