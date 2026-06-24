def solution(n, w, num):
    # 레벨 1이라 그런지 매우 쉽군
    m = n // w + 1
    board = [[0 for _ in range(w)] for _ in range(m)]
    count = 1
    check = 0
    answer = [1]
    if (m - 1) % 2 == 0:
        check = 1
    else:
        check = 0
    
    for i in range(m-1, -1, -1):
        for j in range(w):
            if count  == n + 1:
                break
            if check == 1:
                if i % 2 == 0:
                    board[i][j] = count
                    count +=1
                else:
                    board[i][w-j-1] = count
                    count +=1
            else:
                if i % 2 != 0:
                    board[i][j] = count
                    count +=1
                else:
                    board[i][w-j-1] = count
                    count +=1
    check = 0
    for i in range(m):
        for j in range(w):
            if board[i][j] == num:
                check = 1
                while i >0:
                    i -= 1
                    if board[i][j] != 0:
                        answer.append(1)
                if check == 1:
                    return sum(answer)
                    
    
    
    