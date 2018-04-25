a = input().split()
for word in a:
		new_word = word.replace("apa", "a")
		new_word = new_word.replace("epe", "e")
		new_word = new_word.replace("ipi", "i")
		new_word = new_word.replace("opo", "o")
		new_word = new_word.replace("upu", "u")
		print(new_word,end=" ")
