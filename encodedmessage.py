import math

a = int(input())

for i in range(a):
	message = input()
	encrypted = [' '] * len(message)
	s = int(math.sqrt(len(message)))
	t = 0
	for j in range(s):
		for k in range(s):
			encrypted[len(message) - (k+1)*s + j] = message[t]

			t += 1
	print("".join(encrypted))