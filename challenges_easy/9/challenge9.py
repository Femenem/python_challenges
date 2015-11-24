#!usr/bin/python3
digits = []
for digit in input("enter "):
	digits.append(digit)
digits.sort()
for digit in digits:
	print(digit)