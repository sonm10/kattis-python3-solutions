def alternate(small,big,stars):
	for i in range(1,stars//small):
		if (small*i + big*i) == stars or (small*i + big*(i+1)) == stars:
			return str(big)+","+str(small)


def same(num,stars):
	if (stars%num == 0):
		return str(num)+","+str(num)

stars = int(input())
flags = []

for i in range(1,(stars+1)//2):
	alternate_flags = alternate(i,i+1,stars)
	if alternate_flags is not None:
		flags.append(alternate_flags)
	same_flags = same(i+1,stars)
	if same_flags is not None:
		flags.append(same_flags)
print(str(stars)+":")
for flag in flags:
	print(flag)