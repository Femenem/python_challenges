#!usr/bin/python3
bestStudent = {}
f = open('Desktop/python/lessons/studentgrades.txt')
for line in f:
	name, grade = line.split()
	bestStudent[grade] = name
	
f.close()

bestStudentStr = ""

for i in sorted(bestStudent.keys(), reverse=True):
	print(bestStudent[i] + "scored a" + i)
	bestStudentStr += bestStudent[i] + " scored a " + i + "\n"

	print(bestStudentStr)
bestStudentStr = "\nThe best students ranked \n\n" + bestStudentStr

outToFile = open("Desktop/python/lessons/studentrank.txt", mode="w", encoding="utf-8")
outToFile.write(bestStudentStr)
outToFile.close()
print("Finished update")
