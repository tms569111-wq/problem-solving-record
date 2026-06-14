def solution(today, terms, privacies):
    year,month,day=today.split(".")
    year=int(year)
    month=int(month)
    day=int(day)
    answer = []
    count=1
    for i in privacies:
        date,term=i.split(" ")
        i_year, i_month, i_day=date.split(".")
        i_year=int(i_year)
        i_day=int(i_day)
        time=0
        for j in terms:
            if term in j:
                qwe,m=j.split(" ")
                time=int(m)
        all_month=int(i_month)+time
        if all_month//12>=1:
            i_year+=all_month//12
            all_month=all_month%12
            if all_month==0:
                all_month=12
                i_year-=1
        if year>i_year:
            answer.append(count)
        elif year==i_year and month>all_month:
            answer.append(count)
        elif year>=i_year and month>=all_month and day>=i_day:
            answer.append(count)
        count+=1
    
    return answer