import math
def solution(fees, records):
    dt,df,ut,uf=fees
    in_time={}
    total_time={}
    
    for r in records:
        time,num,status=r.split()
        h,m=map(int, time.split(':'))
        minutes=h*60+m
        if status=="IN":
            in_time[num]=minutes
        else:
            total_time[num]=total_time.get(num,0)+minutes-in_time[num]
            del in_time[num]
    for num,time in in_time.items():
        total_time[num]=total_time.get(num,0)+1439-time
    answer=[]
    for num in sorted(total_time.keys()):
        time=total_time[num]
        if time<=dt:
            fee=df
        else:
            fee=df+math.ceil((time-dt)/ut)*uf
        answer.append(fee)
    return answer