import re

def solution(my_string):
    numbers = re.sub(r'[^0-9]', ' ', my_string)
    return sum(int(n) for n in numbers.split())