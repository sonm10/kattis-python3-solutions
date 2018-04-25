a = int(input())

for i in range(a):
	count = int(input())

	guests = input().split()

	for guest in guests:
		if guests.count(guest) == 1:
			print("Case #{}: {}".format(i+1,guest))
			break
