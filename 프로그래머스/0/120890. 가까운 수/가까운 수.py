def solution(array, n):
    very_close=999999
    for i in array:
        if abs(i-n)<abs(very_close-n):
            very_close=i
        elif abs(i - n) == abs(very_close - n):
            if i < very_close:
                very_close = i
    answer = very_close
    return answer