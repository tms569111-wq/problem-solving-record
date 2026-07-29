# 트라이를 쓰는 문제
# class를 만들고 self node랑 child count를 만들어서 세고
# count 만큼 더하면 되는 문제
# 
def common_prefix_length(word1, word2):
    length = min(len(word1), len(word2))
    
    for i in range(length):
        if word1[i] != word2[i]:
            return i
    return length


def solution(words):
    words.sort()
    answer = 0
    
    for i, word in enumerate(words):
        previous_common = 0
        next_common = 0
        
        if i > 0:
            previous_common = common_prefix_length(
                word,
                words[i - 1]
            )
        if i < len(words) - 1:
            next_common = common_prefix_length(
                word,
                words[i + 1]
            )
        required = max(previous_common, next_common) + 1
        
        answer += min(len(word), required)
    
    
    return answer