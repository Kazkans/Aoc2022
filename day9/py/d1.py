h=[0,0]
t=[0,0]

been=set(t)

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
        h[0]+=1
    if d ==  "L":
        h[0]-=1
    if d ==  "U":
        h[1]+=1
    if d ==  "D":
        h[-1]-=1
    if not touching(h,t):
        zD = norm(h[0]-t[0])
        oD = norm(h[1]-t[1])
        t[0]+=zD
        t[1]+=oD
        been.add(str(t))


with open("input.txt",'r') as f:
    for line in f:
        part=line.split()
        for i in range(0,int(part[1])):
            move(part[0])
print(len(been))
