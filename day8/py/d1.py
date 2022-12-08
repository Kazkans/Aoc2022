grid=[]

col_r=[]
col_l=[]

row_t=[]
row_b=[]

with open("input.txt", 'r') as f:
    for row in f:
        grid.append([])
        for col in row.strip():
            grid[-1].append(int(col))

for r in range(1, len(grid)):
    col_r.append([grid[r][0]])
    for i in range(1,len(grid[r])-1):
        if col_r[-1][-1]<grid[r][i]:
            col_r[-1].append(grid[r][i])
        else:
            col_r[-1].append(col_r[-1][-1])
    col_l.append([grid[r][-1]])
    for i in range(2,len(grid[r])):
        if col_l[-1][-1]<grid[r][-i]:
            col_l[-1].append(grid[r][-i])
        else:
            col_l[-1].append(col_l[-1][-1])
for c in range(1,len(grid[0])-1):
    row_t.append([grid[0][c]])
    for i in range(1,len(grid[0])-1):
        if row_t[-1][-1]<grid[i][c]:
            row_t[-1].append(grid[i][c])
        else:
            row_t[-1].append(row_t[-1][-1])
    row_b.append([grid[-1][c]])
    for i in range(2,len(grid[0])):
        if row_b[-1][-1]<grid[-i][c]:
            row_b[-1].append(grid[-i][c])
        else:
            row_b[-1].append(row_b[-1][-1])
            
v=0
for i in range(1,len(grid)-1):
	for j in range(1, len(grid[i])-1):
		#print(i,j, grid[i][j], col_l[i-1][-j-1])
		if grid[i][j]>col_r[i-1][j-1] or \
		   grid[i][j]>col_l[i-1][-j-1] or \
		   grid[i][j]>row_t[j-1][i-1] or \
		   grid[i][j]>row_b[j-1][-i-1]:
				v+=1
maxS=0
for i in range(1,len(grid)-1):
	for j in range(1,len(grid[i])-1):
		score1=0
		score2=0
		score3=0
		score4=0

		for k in range(j+1,len(grid)):
			score1+=1
			if not grid[i][k]<grid[i][j]:
				break
		for k in range(1,j+1):
			score2+=1
			if not grid[i][j-k]<grid[i][j]:
				break
		for k in range(i+1,len(grid)):
			score3+=1
			if not grid[k][j]<grid[i][j]:
				break
		for k in range(1,i+1):
			score4+=1
			if not grid[i-k][j]<grid[i][j]:
				break
		score=score1*score2*score3*score4
		if maxS<score:
			maxS=score

print(len(grid)*4-4+v)
print(maxS)
