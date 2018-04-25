user_i = input().split()

R,C,r,c = user_i[0],user_i[1],user_i[2],user_i[3]

article = []
for i in range(int(R)):
	article.append(input())
for row in range(len(article)):
	string = article[row]
	new_string = ""
	for x in list(string):
		new_string += x * int(c)
	article[row] = new_string

for i in range(len(article)):
	for j in range(int(r)):
		print(article[i])