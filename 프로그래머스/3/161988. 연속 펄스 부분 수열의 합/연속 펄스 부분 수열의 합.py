def solution(sequence):
    # 일단 감이 안 오네...
    # 1~len(sequence)만큼 수열 조합으로 만들면서 하면 완전탐색 되긴 하나
    # 아마 시간 복잡도로 타임오버
    # 차라리 아예 모든 sequence를 1부터 -1까지 연속해서 펄스로 하는 것과 -1부터 1까지로 하는 것 2개를 만든다.
    # 그뒤 투포인터 느낌으로 하기?
    # 투포인터를 음수 포함 된 정수 수열에서 최대값 구하기로 어떻게 해야 할까.
    # 결국 못풀어서 답 보니까 dp로 푸네
    # 이걸 어캐 암;;;
    seq_minus=[((-1)**i)*sequence[i] for i in range(len(sequence))]
    seq=[((-1)**(i+1))*sequence[i] for i in range(len(sequence))]
    def max_subarray(arr):
        current = arr[0]
        answer = arr[0]
        
        for i in range(1,len(arr)):
            current = max(arr[i], current + arr[i])
            answer = max(answer,current)
        return answer
    
    return max(max_subarray(seq_minus), max_subarray(seq))