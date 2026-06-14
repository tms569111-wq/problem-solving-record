def solution(array):
    median=int(len(array)/2)
    array=sorted(array)
    answer=array[median]
    return answer