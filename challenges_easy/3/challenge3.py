#!usr/bin/python3
import os, sys, string
def get_string():
	print("Enter the text you want to cipher: ")
	return input()

def get_key():
	keyInput = input("Enter the ammount you want to cipher by: ")
	keyInput = int(keyInput)
	return keyInput

def cipher(cipherString, key):
	stringLength = len(cipherString)
	number = 0
	tempList = []
	while number < stringLength:
		if cipherString[number] ==  "Z":
				tempLetter = "A"
				newOrd = ord(tempLetter) + (key-1)
				tempList.append(chr(newOrd))

		elif cipherString[number] ==  "z":
				tempLetter = "a"
				newOrd = ord(tempLetter) + (key-1)
				tempList.append(chr(newOrd))

		elif ord(cipherString[number]) >= 65 and ord(cipherString[number]) <= 90 or ord(cipherString[number]) >= 97 and ord(cipherString[number]) <= 122:
			newOrd = ord(cipherString[number]) + key
			tempList.append(chr(newOrd))

		elif cipherString[number] ==  " ":
			tempList.append(" ")



		number = number + 1
	new_string =''.join(tempList)
	return new_string


inputString = get_string()
keyNumber = get_key()
new_string = cipher(inputString, keyNumber)
print(new_string)

