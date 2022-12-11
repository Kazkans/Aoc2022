rope=[]
for i in range(0,10):
    rope.append([0,0])

been=set()
been.add(tuple(rope[9]))

def touching(h,t):
    if abs(h[0]-t[0])<=1 and abs(h[1]-t[1])<=1:
        return True
    else:
        return False

def norm(a):
    if a!=0:
        return a/abs(a)
    else:
        return a
def move(d):
    if d == "R":
        rope[0][0]+=1
    if d ==  "L":
        rope[0][0]-=1
    if d ==  "U":
        rope[0][1]+=1
    if d ==  "D":
        rope[0][-1]-=1
    for i in range(0,9):
        if not touching(rope[i],rope[i+1]):
            zD = norm(rope[i][0]-rope[i+1][0])
            oD = norm(rope[i][1]-rope[i+1][1])
            rope[i+1][0]+=zD
            rope[i+1][1]+=oD
            
    been.add(tuple(rope[9]))


with open("input.txt",'r') as f:
    for line in f:
        part=line.split()
        for i in range(0,int(part[1])):
            move(part[0])
print(len(been))
