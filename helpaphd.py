a = int(input())
for i in range(a):
	op = input()
	if op == "P=NP":
		print("skipped")
	else:
		first = int(op.split('+')[0])
		second = int(op.split('+')[1])
		print(first+second)