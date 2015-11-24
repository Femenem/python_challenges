#!usr/bin/python3
import os, sys, random, string

def randomword(length):
	return ''.join(random.choice(string.lowercase) for i in range(length))

length = input("How long would you like this password to be? ")
print(randomword(length))