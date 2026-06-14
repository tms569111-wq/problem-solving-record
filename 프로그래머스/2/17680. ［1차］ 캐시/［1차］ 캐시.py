def solution(cacheSize, cities):
    page=[]
    recently=[]
    cacheSize_now=0
    answer = 0
    for i in range(len(cities)):
        cities[i]=cities[i].lower()
    for i in range(len(cities)):
        if cacheSize==0:
            return len(cities)*5
        if cacheSize_now<cacheSize and cities[i] not in page:
            cacheSize_now+=1
            page.append(cities[i])
            for j in range(len(recently)):
                recently[j]+=1
            recently.append(0)
            answer+=5
        elif cities[i] in page:
            answer+=1
            ind=page.index(cities[i])
            for j in range(len(recently)):
                if j!=ind:
                    recently[j]+=1
                elif j==ind:
                    recently[j]=0
        elif cities[i] not in page:
            ind=recently.index(max(recently))
            for j in range(len(recently)):
                if j!=ind:
                    recently[j]+=1
                elif j==ind:
                    recently[j]=0
            page[ind]=cities[i]
            answer+=5
    return answer