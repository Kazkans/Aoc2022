win = {
    'A':2,
    'B':3,
    'C':1,
}
lose = {
    'A':3,
    'B':1,
    'C':2,
}

with open("input.txt", 'r') as f:
    score=0
    for line in f:
        pair = line.strip().split()
        if pair[1]=="X":
            score+=lose[pair[0]]
        elif pair[1]=='Z':
            score+=win[pair[0]]+6
        else:
            score+=ord(pair[0])-ord("A")+1+3
    print(score)
