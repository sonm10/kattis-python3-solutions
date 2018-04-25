tiners = input().split(" ")
l = int(tiners[0])
r = int(tiners[1])

if l == 0 and r ==0:
	print("Not a moose")
elif l == r:
	print("Even "+str(r*2))
else:
	print("Odd "+str(l*2 if l>r else r*2))
