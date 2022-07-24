def add(numList):
    if len(numList)!=4:
        return -1;
    s=0;
    for i in numList:
        if int(i)%2==0:
            s+=int(i)
    if s==0:
        return 0;
    return s;
