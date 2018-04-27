l = int(input())
d = int(input())
x = int(input())

for i in range(l-1,d+1):
	string = list(str(i))
	sum = 0
	for j in string:
		sum += int(j)
	if sum == x:
		print(i)
		break
for i in range(d+1,l-1,-1):
	string = list(str(i))
	sum = 0
	for j in string:
		sum += int(j)
	if sum == x:
		print(i)
		break