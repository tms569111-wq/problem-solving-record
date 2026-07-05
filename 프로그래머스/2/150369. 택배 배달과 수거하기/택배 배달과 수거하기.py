def solution(cap, n, deliveries, pickups):
    # 이거 방법이 여러개 있는데 bfs나 dfs로 해야 하나..
    # 일단 cap이 50이니까 cap이 0일 때 부터 50일 때까지?
    # 근데 만약 cap이 50인데 전체 10만이고 각 집에서 50개 배달해야 하면
    # cap 50 ** 10만?
    # bfs나 dfs가 아닌 것 같음...
    # 완전탐색?
    # 얘도 애매함
    # greedy같은데 
    # 내 생각에는 결국 모든 배달과 수거를 마쳐야 하니까 끝까지 가긴 가야 함
    # 이거 그러니까 멀리 있는 놈을 먼저 하는게 수거 및 배달에서 최대치를 먹을 수 밖에 없음
    # 그러니까 먼놈 순서대로 처리 하는 걸로 해보자.
    # 문제는 n이 10만이란 것, 먼놈 순서대로 1부터 왔다갔다 10만 부터 99000까지 50개씩 하면 시간 오바 됨
    # 즉, 근데 사실 또 애매한 게 배달과 수거라는 개념임
    # 왜 맨 처음에 택배를 cap만큼 실지 않고 갔지? 
    # 예시 1번에서 택배 3개대신 4개를 실으면 1번째 집에 1개, 5번짐에 2개, 4번 집에 1개 줄텐데
    # 왜 1번집을 살려뒀지
    # 모르겠다. 잘 모르겠어. 어차피 돌아오면서 빈 택배로 배달 하지도 못 하는데
    # 그냥 최대로 주는 경우로 생각하자.
    # 1. 일단 먼저 del_idx와 pick_idx으로 나눠서 다 담기
    deliveries = [0] + deliveries
    pickups = [0] + pickups

    del_idx = []
    pick_idx = []
    for i in range(n + 1):
        if deliveries[i] != 0:
            del_idx.append(i)
        if pickups[i] != 0:
            pick_idx.append(i)
            
    answer = 0
    
    while del_idx != [] or pick_idx != []:
        if del_idx == []:
            answer += pick_idx[-1] * 2
            
            now_cap = cap
            while now_cap > 0:
                if pick_idx == []:
                    break

                if pickups[pick_idx[-1]] != 0:
                    pickups[pick_idx[-1]] -= 1
                    now_cap -= 1
                if pickups[pick_idx[-1]] == 0:
                    pick_idx.pop()
            
        elif pick_idx == []:
            answer += del_idx[-1] * 2
            now_cap = cap
            while now_cap > 0:

                if del_idx == []:
                    break

                if deliveries[del_idx[-1]] != 0:
                    deliveries[del_idx[-1]] -= 1
                    now_cap -= 1
                if deliveries[del_idx[-1]] == 0:
                    del_idx.pop()
        else:
            answer += max(del_idx[-1], pick_idx[-1]) * 2 
        
            now_cap = cap
            while now_cap > 0:

                if del_idx == []:
                    break

                if deliveries[del_idx[-1]] != 0:
                    deliveries[del_idx[-1]] -= 1
                    now_cap -= 1
                if deliveries[del_idx[-1]] == 0:
                    del_idx.pop()

            now_cap = cap
            while now_cap > 0:
                if pick_idx == []:
                    break

                if pickups[pick_idx[-1]] != 0:
                    pickups[pick_idx[-1]] -= 1
                    now_cap -= 1
                if pickups[pick_idx[-1]] == 0:
                    pick_idx.pop()
    return answer