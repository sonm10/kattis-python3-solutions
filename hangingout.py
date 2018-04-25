a = input().split()

L = int(a[0])
t = int(a[1])
count = 0
rejected = 0
for i in range(t):
	string = input().split()
	command = string[0]
	number = int(string[1])
	if command == "enter":
		if number+count > L:
			rejected += 1
		else:
			count += number
	else:
		count -= number
print(rejected)