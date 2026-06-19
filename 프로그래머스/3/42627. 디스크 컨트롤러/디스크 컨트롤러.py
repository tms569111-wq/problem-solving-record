from collections import deque
def solution(jobs):
    # 일단은 비선점 이거 부터 훨씬 쉬울 듯
    # 각 작업 끝날 때마다 반환시간 따로 answer에 저장
    # 0초에서 시작
    # 매 작업 끝날 때마다 우선순위 재정렬
    # 500*을 500번??? 10만번 정도
    # 시간 초과는 안 날 듯
    # 이거 정렬을 먼저 
    # 이거 안 와서 멍때리는 시간이 맹점인듯
    # 멍 때리는 시간 구해야 함
    answer = 0
    for i in range(len(jobs)):
        new = jobs[i]
        new.append(i)
        jobs[i] = new
    now = 0
    jobs.sort(key = lambda x : (x[1], x[0], x[2]))

    n = len(jobs)
    for _ in range(n):
        check = 0
        for i in range(len(jobs)):
            if jobs[i][0] <= now:
                now += jobs[i][1]
                answer += now - jobs[i][0]
                jobs.pop(i)
                check = 1
                break
        if check == 0:
            min_t = 1e9
            idx = 0
            for j in range(len(jobs)):
                if min_t > jobs[j][0]:
                    min_t = jobs[j][0]
                    idx = j
            now = min_t
            now += jobs[idx][1]
            answer += now - jobs[idx][0]
            jobs.pop(idx)
    return answer//n