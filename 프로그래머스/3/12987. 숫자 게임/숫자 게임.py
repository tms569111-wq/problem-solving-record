def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    a_idx = 0
    for b_idx in range(len(B)):
        if B[b_idx] > A[a_idx]:
            answer += 1
            a_idx += 1
            
    return answer
