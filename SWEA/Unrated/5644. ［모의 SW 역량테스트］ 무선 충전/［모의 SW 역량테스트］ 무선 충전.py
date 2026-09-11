from collections import defaultdict
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
dx = [0, 0, 1, 0, -1] 
dy = [0, -1, 0, 1, 0]
for test_case in range(1, T + 1):
    M, bc = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    dic_x_y = defaultdict(list)
    dic_x_y_location = defaultdict(list)
    for k in range(bc):
        x, y, c, p = map(int, input().split())
        for i in range(x - c, x + c + 1):
            for j in range(y - c, y + c + 1):
                if i >= 1 and i <= 10 and  j >= 1 and j<= 10:
                    if abs(x - i) + abs(y - j) <= c:
                        dic_x_y[(i,j)].append(p)
                        dic_x_y_location[(i,j)].append(k)
    answer = 0
    a_now = (1, 1)
    b_now = (10, 10)
    def charge(a_now, b_now):

        a_possible = []

        b_possible = []

        for i in range(len(dic_x_y[a_now])):
            bc_number = dic_x_y_location[a_now][i]
            power = dic_x_y[a_now][i]
            a_possible.append((bc_number, power))

        for i in range(len(dic_x_y[b_now])):
            bc_number = dic_x_y_location[b_now][i]
            power = dic_x_y[b_now][i]
            b_possible.append((bc_number, power))


        if len(a_possible) == 0:
            a_possible.append((-1, 0))

        if len(b_possible) == 0:
            b_possible.append((-1, 0))


        max_charge = 0

        for a_bc, a_power in a_possible:
            for b_bc, b_power in b_possible:
                if a_bc == b_bc:
                    if a_bc == -1:
                        total = 0
                    else:
                        total = a_power
                else:
                    total = a_power + b_power
                max_charge = max(max_charge, total)
        return max_charge

    answer += charge(a_now, b_now)

    for i in range(M):
        a_now = (
            a_now[0] + dx[a_list[i]],
            a_now[1] + dy[a_list[i]]
        )
        b_now = (
            b_now[0] + dx[b_list[i]],
            b_now[1] + dy[b_list[i]]
        )

        answer += charge(a_now, b_now)


    print(f"#{test_case} {answer}")