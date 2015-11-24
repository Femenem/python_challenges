#!usr/bin/python3

#immutible integer
intEx = 1
print(id(intEx))
intEx = 2
print(id(intEx))


#mutable list
listEx = ["Matt"]
print(id(listEx))
listEx.append("Cat")
print(id(listEx))
print("")

tupleEx = ("Matt", 20, "Basingstoke", "HANTS")
for i in tupleEx:
	print(i)

print("First element in tuple is", tupleEx[0])
print("")

list1 = ["Matt", 20, "Basingstoke", "HANTS"]
for x in list1:
	print(x)
list1.append("Joy")
print(list1)

print(list1[4])
list1.remove("Joy")
print(list1)
list1.remove(list1[3])
print(list1)
list1.insert(2, "HANTS")
print(list1)

listEx2 = ["f", "e", "c", "d"]
listEx2.sort()
print(listEx2)

listEx2.reverse()
print(listEx2)


listEx3 = [
	["a", "b", "c"],
	["d", "e", "f"],
	["g", "h", "i"],
	]
print(listEx3[2][1])


dictEx = ({"Age":20, "Height":"6'0", "Weight":150})
print(dictEx)
print(dictEx.get("Height"))
print(dictEx.items())
print(dictEx.values())
dictEx.pop("Height")
print(dictEx)

a, b = 1, 11
while a<b:
	print(a)
	a += 1
print()

for x in [1,2,3,4]:
	print(x)

listCycle = [1,2,3,4]
listCycle[:] = range(1,201)

for i in listCycle:
	print(i)
print()


for i in listCycle:
	if (i%2) == 0:
		continue
	elif (i == 101):
		break
	else:
		print(i)
