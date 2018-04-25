a = int(input())

for i in range(a):
	numbers = input().split()
	number1 = int(numbers[0])
	number2 = int(numbers[1])
	answer = int(numbers[2])
	
	if number1 * number2 == answer or number1 / number2 == answer or number1 + number2 == answer or number1 - number2 == answer:
		print("Possible")
	elif number2 * number1 == answer or number2 / number1 == answer or number2 + number1 == answer or number2 - number1 == answer:
		print("Possible")
	else:
		print("Impossible")