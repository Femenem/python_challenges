#!usr/bin/python3
bottles = 99
number = 1
while number != 101:
	if bottles == 2:
		print(str(bottles)+" bottles of beer on the wall, "+str(bottles)+" bottles of beer.")
		print("Take one down and pass it around, "+str(bottles-1)+" bottle of beer on the wall.")
	elif bottles == 1:
		print(str(bottles)+" bottle of beer on the wall, "+str(bottles)+" bottle of beer.")
		print("Take one down and pass it around, no more bottles of beer on the wall.")
	elif bottles == 0:
		print("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
	else:
		print(str(bottles)+" bottles of beer on the wall, "+str(bottles)+" bottles of beer.")
		print("Take one down and pass it around, "+str(bottles-1)+" bottles of beer on the wall.")
	number = number + 1
	bottles = bottles - 1