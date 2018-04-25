tests = int(input())

for i in range(tests):
	s = input()
	stores = input().split()
	count = 0
	stores.sort(key=int)
	for j in range(int(s)-1,0,-1):
		count += int(stores[j]) -int(stores[j-1])

	print(count*2)