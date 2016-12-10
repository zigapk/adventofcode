asdf = input().split(", ")
smeri = [(1,0),(0,1),(-1,0),(0,-1)]
smer = 0
gor = 0
desno = 0

for item in asdf:
	if item[0] == "R": smer = (smer + 1) % 4
	else: smer = (smer - 1) % 4

	gor += int(item[1:])*smeri[smer][0]
	desno += int(item[1:])*smeri[smer][1]

print(abs(gor)+abs(desno))
