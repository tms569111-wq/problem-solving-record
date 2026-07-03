from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

def solution(nodeinfo):
    # 일단 위에서 부터 정렬
    # y는 크고 x는 작은 순으로 정렬
    # 연결 리스트? 써서 만들어야 될 듯
    # 전위 중위 후위
    # 전위는 중좌우
    # 중위는 좌중우
    # 후위는 좌우중
    # 약간 재귀 느낌으로
    # 전위는 print(중) 하고 preorder(좌)하고 preorder(우)하고 return 하면 되고
    # 후위는 반대로 하면 될 듯
    # 문제는 트리에 넣는 건데
    # 어떤 숫자 인덱스 7의 죄측은 예시에서 4이고, 2는 우측
    # 근데 연결 리스트보다는 dic이 낫나
    # 이거 자구 때 클래스 썼던 것 같은데 기억이 안남 ㅠㅠ
    # 일단 nodeinfo 기준으로 x[1]인 y축이 제일 큰놈이 root되고
    # 그 뒤 y축 2번째로 작은 놈 이 x가 자기보다 작으면 왼쪽 되고
    # x가 크면 오른쪽 되는 걸로 계산
    # 그래서 만들면 재귀로 출력인데트리 깊이가 1000이하라면
    # 굳이 recursive안 해도 될 듯
    # 트리 만드는 거 개빡세네. 3 의 자식이 5가 아니고 8의 자식이 5이려면 
    # 아 root의 것 보다 오른쪽인데 작으면 안 되서
    # 이거 수천번 연산 각인데...일단 하자
    
    nodes = []
    for idx, (x, y) in enumerate(nodeinfo, 1):
        nodes.append([x, y, idx])
    
    nodes.sort(key = lambda x : (-x[1], x[0]))
    x_dic = {}
    for x, y, idx in nodes:
        x_dic[idx] = x

    
    left_dic = defaultdict(lambda : -1)
    right_dic = defaultdict(lambda : -1)
    
    root = nodes[0][2]
    
    for x, y, idx in nodes[1:]:
        now = root
        while True:
            if x < x_dic[now]:
                if left_dic[now] == -1:
                    left_dic[now] = idx
                    break
                now = left_dic[now]
            else:
                if right_dic[now] == -1:
                    right_dic[now] = idx
                    break
                now = right_dic[now]
    preorder = []
    postorder = []
    def dfs(now):
        if now == -1:
            return
        preorder.append(now)
        dfs(left_dic[now])
        dfs(right_dic[now])
        
        postorder.append(now)
    dfs(root)
    
    return [preorder, postorder]