def solution(myStr):
    for char in ['a', 'b', 'c']:
        myStr = myStr.replace(char, ',')
    split_str = myStr.split(',')
    answer = [s for s in split_str if s != ""]
    return answer if answer else ["EMPTY"]