#!usr/bin/python3
import os, sys

username = "Matt"
password = "aadjkghiuhakljnhlvaioahjv"

usernameGiven = input("Please enter your username: ")
passwordGiven = input("Please enter your password: ")

if usernameGiven == username and passwordGiven == password:
	print("You have been logged in!")
else:
	print("Wrong password")