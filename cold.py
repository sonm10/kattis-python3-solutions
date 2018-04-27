a = input()

temp = input().split()

print(sum(1 for i in temp if int(i) < 0))