# 음식을 라운드 로빈의 형식으로 먹고 있음...
# K초 후네트워크 장애로 방송이 중단
# k는 너무너무 크기 때문에 완전탐색이 불가능
# 일단 food_times 길이가 지나면 전체가 1씩 빠짐
# 즉 k를 food_times의 길이를 나눈 몫만큼 전체원소에서 빼고
# k와 food_times의 나머지 위치가 원래 모든 food_times가 꽉꽉채워졌을 때 먹어야 하는 곳
# 그런데 어떤 걸 다 먹으면 -n만큼 되어있을 거임
# 그 부담은 어디로?
# 다시 반복하기에는 food_times의 길이가 20만임
# 아니면 sort?
# 최솟값으로 sort하고 맨 처음 원소부터 k를 빼기 시작
# k가 0이 될 때의 원소로?
# 이거 둘 다 해야 되네
# 최소값 * len(food_times) 보다 k가 작으면 나머지로 구하고
# 아니면 k - 최소값 * len(food_times)하고
# 그 다음은 k - 최소값[1] * (len(food_times) - 1)하고
# 그러다가 나머지
# 이거 시간복잡도가 할 만 하네
def solution(food_times, k):
    if len(food_times) == 1:
        return 1
    if sum(food_times) <= k:
        return -1
    n = len(food_times)
    count = 0
    new_list = [0] + [i + 1 for i in range(n)]
    food_list = [[] for _ in range(n)]
    for i in range(n):
        food_list[i] = [food_times[i], i + 1]
    food_list.sort(key = lambda x:x[0])
    
    for i in range(len(food_list)):
        count = count + food_list[i][0]
        if k - (food_list[i][0] * n) < 0:
            check = k % n + 1
            
            for j in range(1, 1 + len(food_list)):
                if new_list[j] != 0:
                    check -= 1
                if check == 0:
                    return new_list[j]
            
        else:
            k -= (food_list[i][0] * n)
            n = n - 1
            new_list[food_list[i][1]] = 0
            if n == 0:
                return -1
            food_list[i + 1][0] -= count
            