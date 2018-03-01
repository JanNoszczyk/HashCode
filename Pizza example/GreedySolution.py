f = open('example.in','r')
first_line = f.readline()

row_count, column_count, min_ingredient, max_area = tuple(map(int,first_line.split(' ')))

grid = []
for i in range(row_count):
	grid.append(f.readline().rstrip())

f.close()

results = []
#For each row, I reset the counter
for r in range(row_count):
	beg = 0
	end = 0
	mushroom_count = 0
	tomato_count = 0
#While I'm not at the end of the tow, I count if I 
#have a tomato or mushroom
while end < column_count:
	if grid[r][end] == 'M':
		mushroom_count += 1
	elif grid[r][end] == 'T':
		tomato_count += 1
	end += 1
#If the slice is too big, I must remove an ingredient
	if end - beg > max_area:
		if grid[r][beg] == 'M':
			mushroom_count -= 1
		elif grid[r][beg] == 'T':
			tomato_count -= 1
		beg += 1
		#If we havea valid slice, we log it in
		#the results and reset the variables,
		#in order to continue searching for
		#new valid sliced in the same line
	if (end-beg<=max_area and mushroom_count>=min_ingredient and tomato_count>=min_ingredient):
		results.append((r,beg,r,end-1))
		beg = end
		tomato_count = 0
		mushroom_count = 0
