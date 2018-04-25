def fib(a):
	b,c = 3,5
	if a == 1:
		return b
	elif a == 2:
		return c
	else:
		for i in range(a - 2):
			b,c = c,(((c - b) * 2) + c)
		return c		

iteration = int(input())


print(fib(iteration) ** 2)

