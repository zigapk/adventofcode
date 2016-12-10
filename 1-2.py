import sys


asdf = input().split(", ")
smeri = [(1,0),(0,1),(-1,0),(0,-1)]
smer = 0
gor = 0
desno = 0
visited = [(0, 0)]

for item in asdf:
	if item[0] == "R": smer = (smer + 1) % 4
	else: smer = (smer - 1) % 4

	koraki = int(item[1:])
	for i in range(koraki):
		gor += 1*smeri[smer][0]
		desno += 1*smeri[smer][1]
		if (gor, desno) in visited:
			print(abs(gor)+abs(desno))
			sys.exit()
		else:
			visited.append((gor, desno))
