import re

def solution(files):
    temp = []
    for file in files:
        parts = re.split(r'([0-9]+)', file)
        
        head = parts[0]
        number = parts[1]
        temp.append((file, head.lower(), int(number)))
    temp.sort(key=lambda x: (x[1], x[2]))
    
    return [t[0] for t in temp]
