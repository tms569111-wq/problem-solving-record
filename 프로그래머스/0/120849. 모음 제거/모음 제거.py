def solution(my_string):
    vowels = "aeiouAEIOU"
    return "".join([char for char in my_string if char not in vowels])
