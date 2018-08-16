t = int(input())
strs = []

for i in range(t):
	strs.append(str(input()))

for i in range(t):
	pre, pos = "", ""
	for j in range(len(strs[i])):
		if(j%2 == 0):
			pre += strs[i][j]
		else:
			pos += strs[i][j]
	print("%s %s" % (pre, pos))
			
