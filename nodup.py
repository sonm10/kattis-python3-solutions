import code
str = input()

words = str.split(" ")
bool = False
for word in words:
	if words.count(word) > 1:
		bool = True

if bool == True:
	print("no")
else:
	print("yes")