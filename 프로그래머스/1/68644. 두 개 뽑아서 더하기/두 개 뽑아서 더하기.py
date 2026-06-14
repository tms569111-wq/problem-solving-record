def solution(numbers):
    a=len(numbers)
    answer = []
    for i in range(a):
        for j in range(i+1, a):
            z=numbers[i]+numbers[j]
            if z not in answer:
                answer.append(z)
                
    answer.sort()
    return answer