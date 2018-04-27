a = int(input())
b = int(input())
avail  = a
for i in range(b):
	c = int(input())
	avail -= c
	avail += a

print(avail)