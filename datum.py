import datetime

date = input()

date_f = datetime.datetime.strptime(date+" 2009","%d %m %Y")

print(date_f.strftime("%A"))