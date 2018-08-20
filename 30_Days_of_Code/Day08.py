n = int(input())

books = {}
for i in range(n):
	name, phone = input().split(' ')
	books[name] = phone

name = input()
while(name):
	phone = books.get(name, None)
	if(phone):
		print("%s=%s" % (name, phone))
	else:
		print("Not found")

	name = input()

