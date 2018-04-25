def first(team,teams,index):
	for i in range(index):
		if teams[i].split(" ")[0] == team.split(" ")[0]:
			return False	
	return True

count = int(input())
teams = []
for i in range(count):
	teams.append(input())

winners = []
for i,team in enumerate(teams):
	if first(team,teams,i):
		winners.append(team)
	if len(winners) > 11:
		break

for winner in winners:
	print(winner)