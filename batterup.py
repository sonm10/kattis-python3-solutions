count = int(input())
bats_input = input()
sum = 0
bats = bats_input.split(" ")

for bat in bats:
	if int(bat) < 0:
		count -= 1
	else:
		sum += int(bat)

print(sum/count)