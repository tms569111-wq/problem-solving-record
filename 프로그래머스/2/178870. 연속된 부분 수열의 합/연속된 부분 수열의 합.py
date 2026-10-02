def solution(sequence, k):
    left = 0
    length = [10 ** 10]
    now_sum = 0
    answer = [0, 0]
    for right in range(len(sequence)):
        now_sum += sequence[right]
        if now_sum == k:
            new_length = right - left
            if new_length < length[0]:
                answer[0] = left
                answer[1] = right
                length[0] = new_length
        elif now_sum < k:
            continue
        while now_sum > k:
            now_sum -= sequence[left]
            left += 1
            if now_sum == k:
                new_length = right - left
                if new_length < length[0]:
                    answer[0] = left
                    answer[1] = right
                    length[0] = new_length
            
    return answer