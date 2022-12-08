wins = [["A", "Y"],["B", "Z"], ["C", "X"]]
draws  = [["A", "X"],["B", "Y"], ["C", "Z"]]
with open("input.txt",'r') as f:
    score=0
    for line in f:
        pair=line.strip().split()
        if pair in wins:
            score+=6
        elif pair in draws: 
            score+=3
        score+=ord(pair[1])-ord('X')+1
    print(score)
