def solution(arr, query):
    for i in range(len(query)):
        q = query[i]
        if i % 2 == 0:
            # 짝수 인덱스: query[i] 뒷부분을 자름 (0 ~ q까지 유지)
            arr = arr[:q + 1]
        else:
            # 홀수 인덱스: query[i] 앞부분을 자름 (q ~ 끝까지 유지)
            arr = arr[q:]
    return arr