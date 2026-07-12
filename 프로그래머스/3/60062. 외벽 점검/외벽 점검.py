from itertools import permutations
# 굉장히 신기방기한 문제
# 일단 weak가 있다고 했을 때
# 친구들은 weak가 가장 밀집한 곳에서 부터 시작해서
# 가장 긴 친구가 밀집한 곳을 모두 처리하는 게 제일 좋음
# 즉, greedy 그리디로 풀어야함
# 즉, dist가 가장 긴 친구가 n 0지점부터 200까지 누적으로 했을 때 제일 많은 weak를 건드리는 경우
# n은 최대 200이고 친구는 100명 정도 이므로
# 완전탐색 해봐야 2만정도
# 만약 0부터 weak 볼 때 마다 weak원소를 다 보더라도
# 16 정도라서 30만번 안에 끝난다.
# 문제는 원 이라는 것!
# 그리고 시계 반시계는 그냥 범위로 구하면 되니까 상관 없다
# 이제 할만 하구먼
# 게다가 보니까 n을 다할 필요도 없네. 취약점이 무조건 정수니까 weak위에서 친구의 dist가 움직여야
# 무조건 최대네
# 즉 weak의 원소 15만 곱하면 됨
# 그런데??? 
# 저 덮는 부분인 최대가 여러개라면?
# 일단 내 생각에는 dfs인 것이다.
# 그런데? dfs인 weak가 16개라면? dist는 8이니까
# 16 * 16 * 16 * 16
# 256 * 256
# 5만 * 5만
# 25억...
# 근데 dist가 무조건 하나씩은 빼니까
# 16 * 15 * 14 * 13 * 12 * 11 * 10 * 9
# 대충 160 ** 4
# 그래도 몇 억이네...흠...
# 먼저 dist부터 역정렬 한다.
# 아 완전탐색이었네?
# lru써서 dp 완전탐색

def solution(n, weak, dist):
    
    weak_count = len(weak)
    
    weak_line = weak + [point + n for point in weak]
    answer = len(dist) + 1
    for start in range(weak_count):
        for friends in permutations(dist):
            friend_count = 1
            cover_until = weak_line[start] + friends[0]
            for weak_index in range(start, start + weak_count):
                if weak_line[weak_index] <= cover_until:
                    continue
                friend_count += 1
                if friend_count > len(dist):
                    break
                cover_until = (weak_line[weak_index] + friends[friend_count -1])
            answer = min(answer, friend_count)
            
        
    if answer > len(dist):
        return -1
    return answer
    