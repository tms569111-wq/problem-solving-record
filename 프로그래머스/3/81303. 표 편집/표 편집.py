def solution(n, k, cmd):
    up = [i - 1 for i in range(n)]
    down = [i + 1 for i in range(n)]
    
    down[n - 1] = -1
    
    deleted = []
    cur = k
    
    for command in cmd:
        if command[0] == "U":
            x = int(command.split()[1])
            for _ in range(x):
                cur = up[cur]
    
        elif command[0] == "D":
            x = int(command.split()[1])
            for _ in range(x):
                cur = down[cur]
                
        elif command[0] == "C":
            deleted.append(cur)
            
            upper = up[cur]
            lower = down[cur]
            if upper != -1:
                down[upper] = lower
            if lower != -1:
                up[lower] = upper
            if lower != -1:
                cur = lower
            else:
                cur = upper
        else:
            restore = deleted.pop()
            upper = up[restore]
            lower = down[restore]
            
            if upper != -1:
                down[upper] = restore
            if lower != -1:
                up[lower] = restore
    answer = ["O"] * n
    for row in deleted:
        answer[row] = "X"
    return "".join(answer)
        
        