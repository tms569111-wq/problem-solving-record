def solution(num_list):
    haeol=''
    z=''
    for i in num_list:
        if i%2==1:
            haeol=haeol+str(i)
        else:
            z=z+str(i)
        
    return int(haeol)+int(z)