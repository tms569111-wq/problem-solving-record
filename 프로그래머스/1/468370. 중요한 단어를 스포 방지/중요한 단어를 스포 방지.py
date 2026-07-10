# 걍 set 쓰는 문제 같은데
def solution(message, spoiler_ranges):
    new_message = ''
    now_spo_idx = 0
    n = len(spoiler_ranges)
    for i in range(len(message)):
        if now_spo_idx == n:
            new_message += message[i]
            continue
        if i > spoiler_ranges[now_spo_idx][1]:
            now_spo_idx += 1
        if now_spo_idx == n:
            new_message += message[i]
            continue
            
        if spoiler_ranges[now_spo_idx][0]<= i and i <= spoiler_ranges[now_spo_idx][1]:
            if message[i] == ' ':
                new_message += ' '
            else:
                new_message += '#'
        else:
            new_message += message[i]
    word_list = []
    word_list = message.split(" ")
    
    new_message_list = []
    new_message_list = new_message.split(" ")
    
    set_message = set(word_list)
    new_set = set()
    for i in range(len(new_message_list)):
        if '#' in new_message_list[i]:
            continue
        else:
            new_set.add(new_message_list[i])
    
    answer = len(set_message) - len(new_set)
    return answer