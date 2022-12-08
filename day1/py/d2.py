with open("input.txt", 'r') as f:
    cur=0
    top=[0,0,0]
    for line in f:
        if line.strip()=="":
            for i in range(0,3):
                if cur>top[i]:
                    top=top[:i]+[cur]+top[i:2]
                    break
            cur=0
        else:
            cur+=int(line)
    print(top)
    print(sum(top))
