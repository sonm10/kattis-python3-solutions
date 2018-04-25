def checkAnswer(answer,person):
	seq = len(person)
	count = 0
	for i in range(len(answer)):
		if answer[i] == person[i%seq]:
			count += 1
	return count

q = input()
answers = input()

adrian = "ABC"
bruno = "BABC"
goran = "CCAABB"

adrian_answer = checkAnswer(answers,adrian)
bruno_answer = checkAnswer(answers,bruno)
goran_answer = checkAnswer(answers,goran)

max = max(adrian_answer,bruno_answer,goran_answer)
print(max)
if max == adrian_answer:
	print('Adrian')
if max == bruno_answer:
	print('Bruno')
if max == goran_answer:
	print('Goran')	