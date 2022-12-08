stacks=[[]]
with open("input.txt", 'r') as f:
    for line in f:
        if '[' in line:
            for i  in range(1,len(line),4):
                if line[i].isalpha():
                    while  len(stacks)<=(i-1)//4:
                        stacks.append([])
                    stacks[(i-1)//4].append(line[i])
        elif line.strip()=="":
            for s in stacks:
                s.reverse()
        elif "move" in line:
            parts = line.strip().split()
            for i in range(0,int(parts[1])):
                stacks[int(parts[5])-1].append(stacks[int(parts[3])-1].pop())

top=""
for s in stacks:
    top+=str(s.pop())
print(top)
