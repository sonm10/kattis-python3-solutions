count = int(input())

for i in range(count):
	rev = input().split(" ")
	r =int(rev[0])
	e =int(rev[1])
	c =int(rev[2])

	profit = e - c - r
	if profit > 0:
		print("advertise")
	elif profit < 0:
		print("do not advertise")
	else:
		print("does not matter")