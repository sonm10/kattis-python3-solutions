x = int(input())
y = int(input())
if x > 0 and y > 0:
	q = 1
elif x > 0 and y < 0:
	q = 4
elif x < 0 and y < 0:
	q = 3
else:
	q = 2
print(q)