def solution(data, ext, val_ext, sort_by):
    
    # sort(key=lamda x:(x[0],x[1])) 요런식이 아니라 1개만 오나?
    # 일단 자르기 잘 해야 됨
    d=["code","date","maximum","remain"]
    a=d.index(ext)
    arr=[]
    for i in data:
        if i[a]<val_ext:
            arr.append(i)
    arr.sort(key=lambda x:x[d.index(sort_by)])
    return arr