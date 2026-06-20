from collections import defaultdict
def solution(id_list, report, k):
    # 조건이 상당히 많음
    # 일단 신고당한 횟수를 유저 id로 체크하면
    # 각 유저가 누굴 신고했는지...유저 신고 리스트로 넣기
    # 이걸 muzi를 키로 muzi가 신고한 id로 검색
    
    user_report_check = defaultdict(list)
    report_dic = defaultdict(int)
    names = []
    for i in range(len(report)):
        user, rep = report[i].split(" ")
        if rep not in user_report_check[user]:
            user_report_check[user].append(rep)
            report_dic[rep] += 1
    for name in id_list:
        if report_dic[name] >= k:
            names.append(name)
    answer = []
    for repoter in id_list:
        count = 0
        check_list = user_report_check[repoter]
        for check_name in check_list:
            if check_name in names:
                count += 1
        answer.append(count)
    return answer