with open("input.txt", 'r') as f:
    cur=0
    biggest=0
    for line in f:
        if line.strip()=="":
            if cur>biggest:
                biggest=cur
            cur=0
        else:
            cur+=int(line)
    print(biggest)
