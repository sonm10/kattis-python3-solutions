a = int(input())
count = 0
for i in range(a):
	moves = input()
	if not 'CD' in moves:
		count += 1
print(count)