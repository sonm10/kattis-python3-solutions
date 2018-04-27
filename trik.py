a = input()
b = [1,0,0]

for move in a:
	if move == 'A':
		b[0],b[1] = b[1],b[0]
	elif move == 'B':
		b[1],b[2] = b[2],b[1]
	else:
		b[0],b[2] = b[2],b[0]
for i in range(len(b)):
	if b[i] == 1: print(i+1)
