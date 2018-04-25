def word_value(word):
	sum = 0
	for letter in word:
		sum+=int(char_value[letter])
	return sum

def rotate(word,times):
	new_word = ""
	for letter in word:
		number = char_value[letter] + times
		new_word += find_letter(number)
	return new_word

def merge(word1,word2):
	decrypted = ""
	for i,j in zip(word1,word2):
		position = char_value[i]+char_value[j]
		decrypted += find_letter(position) 
	return decrypted
		
def find_letter(number):
	number = number if number < 26 else number%26
	return list(char_value.keys())[number]



message = input()

length = len(message)

keys = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
values = list(range(0,26))
char_value = {key: value for key, value in zip(keys, values)}

first = message[:int(length/2)]

second = message[int(length/2):]

first_value,second_value = word_value(first),word_value(second)

rotate_first,rotate_second = rotate(first,first_value),rotate(second,second_value)

print(merge(rotate_first,rotate_second))
