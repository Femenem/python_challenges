#!usr/bin/python3
bestGrade = 0
bestStudent = ""
f = open('Desktop/python/lessons/studentgrades.txt')
#for line in f:
#	print(line, end="")
#print()

for line in f:
	name, grade = line.split()
	if int(grade) > bestGrade:
		bestGrade = int(grade)
		bestStudent = name

print("Best Grade ", bestGrade)
print("Best Student ", bestStudent)
f.close()

