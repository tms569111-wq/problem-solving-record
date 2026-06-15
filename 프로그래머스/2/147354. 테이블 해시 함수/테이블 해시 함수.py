def solution(data, col, row_begin, row_end):
    col -= 1
    row_begin -= 1
    row_end -= 1
    # 일단 오름 차순 정렬을 해야 함.
    # 값과 인덱스를 따로 저장하고 값으로 정렬.
    # 인덱스를 따로 리스트로 만들기
    # 이것만 해도 벌써 백만 * 상수항
    index_list=[]
    for i in range(len(data)):
        index_list.append([i,data[i][col],data[i][0]])
    
    index_list.sort(key=lambda x : (x[1], -x[2]))

    new_data = []
    for i in range(len(data)):
        index=index_list[i][0]
        new_data.append(data[index])
    a=0
    for i in range(row_begin, row_end+1):
        s=0
        for j in range(len(new_data[0])):
            s += new_data[i][j]%(i+1)
        a^=s
    
    answer = a
    return answer