def solution(myString):
    return "".join(['l' if char < 'l' else char for char in myString])
