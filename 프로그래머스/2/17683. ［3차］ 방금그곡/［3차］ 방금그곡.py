def solution(m, musicinfos):
    # 복잡한 구현 문제
    # 고려해야 할 것 : 멜로디와 악보, 각 음은 1분에 1개씩, 음악이 반복재생 가능
    # 같은 게 여러개면 시간이 긴 것, 시간이 길면 먼저 입력
    # 따라서 musicinfos에서 일단 자료를 쉼표로 잘라야 함.
    # 그리고 음악이 같은지 확인하고, 같으면 시간 길이, 선후 관계, 제목을 저장해야 함.

    code_match=[]
    time=[]
    def new(f):
        f=f.replace("C#","c")
        f=f.replace("D#","d")
        f=f.replace("F#","f")
        f=f.replace("G#","g")
        f=f.replace("A#","a")
        return f
    m=new(m)
    def time_minus(start, last):
        a,b=last.split(":")
        c,d=start.split(":")
        return int(a)*60+int(b)-int(c)*60-int(d)
    for i in musicinfos:
        start, last, name, code = i.split(',')
        code = new(code)
        played_time = time_minus(start, last)
        played_code = (played_time//len(code))*code+code[:played_time%len(code)]
        if m in played_code:
            code_match.append(name)
            time.append(played_time)
    
    if code_match==[]:
        return "(None)"
    max_time=max(time)
    for i in range(len(time)):
        if time[i] == max_time:
            return code_match[i]