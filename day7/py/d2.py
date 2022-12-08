
above10k=[]

pick=float('inf')

class Tree:
    def __init__(self, size, name, parent):
        self.children=[]
        self.size=size
        self.name=name
        self.parent=parent
    def prnt(self):
        print(self.name, self.size)
        for c in self.children:
            c.prnt()

    def calSize(self):
        for c in self.children:
            self.size+=c.calSize()
        if self.size <= 100000 and self.children and self.name != "/":
            above10k.append(self.size)
        return self.size
    def findPick(self):
        global pick
        if self.size>=toFree and pick>self.size:
            pick=self.size
        for c in self.children:
            if c.children:
                c.findPick()

root=Tree(0,"/",0)
cur=root

with open("input.txt", 'r') as f:
    for line in f:
        parse = line.strip().split()
        if parse[0]=="$":
            if parse[1]=="cd":
                if parse[2]=="..":
                    cur=cur.parent
                elif parse[2]=="/":
                    cur=root
                else:
                    for c in cur.children:
                        if c.name==parse[2]:
                            cur=c
                            break
        else:
            if parse[0]=="dir":
                cur.children.append(Tree(0,parse[1],cur))
            else:
                cur.children.append(Tree(int(parse[0]),parse[1],cur))
root.calSize()
unused=70000000-root.size
toFree=30000000-unused
root.findPick()
print(pick)
