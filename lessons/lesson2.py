#!usr/bin/python3
import sys, math, decimal

#Demonstrate integers

x, y, z = 1, 2, 3
print(x,y,z)

print("")

def boolEx(a, b):
	print(type(a))
	print(a and b)
	print(a or b)
	print(not b)
	d = ((1 > 2) and (3 <=3))
	print(d)

def intEx():
	x = 5
	y = 2
	print("X + y = ", x+y)

	print("{} + {} = ".format(x, y), x+y)
	print("{} - {} = ".format(x, y), x-y)
	print("{} * {} = ".format(x, y), x*y)
	print("{} / {} = ".format(x, y), x/y)
	print("{} % {} = ".format(x, y), x%y)
	print("{} ** {} = ".format(x, y), x**y)

	print("")

	print("Binary format for 4", bin(4))
	print(float(x))
	print(pow(x,y))
	print("")

	z = 100/3
	print(round(z,3))
	print(math.ceil(z))
	print(math.floor(z))
	print("")

	z = 1.234567891011
	print(z)
	z = decimal.Decimal("1.234567891011121314151617")
	print(z)

boolEx(True, False)
intEx()