def solution(mats, park):
    # 2차원 배열 돌아가면서 5, 3, 2를 오른쪽 + 아래 쪽으로 하되 -1이 아니라면 포기
    # 3중 for문 maybe
    answer=[-1]
    right=len(park)
    upper=len(park[0])
    for i in range(len(park)):
        for j in range(len(park[i])):
            for mat in mats:
                if 0<=i+mat<=right and 0<=j+mat<=upper:
                    check=0
                    for k in range(i,i+mat):
                        for l in range(j,j+mat):
                            if park[k][l]!="-1":
                                check=1
                                break
                    if check==0:
                        answer.append(mat)
    return max(answer)