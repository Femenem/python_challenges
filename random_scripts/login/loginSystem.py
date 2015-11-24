#!/usr/bin/python3
import sqlite3
import sys

def newUser():
	usernameGiven = input("Please enter a valid username type exit to exit: ")
	if usernameGiven == "exit":
		exit()
	passwordGiven = input("Please enter a password: ")
	passwordGiven2 = input("Please enter the same password again: ")
	if passwordGiven == passwordGiven2:
		cDB.execute("INSERT INTO users VALUES (?, ?);", (usernameGiven, passwordGiven))
	else:
		print("Password was not the same! Please try again")
		newUser()

def loginUser():
	loginUsername = input("Please enter your username: ")
	loginPassword = input("Please enter your password: ")
	cDB.execute("SELECT username, password FROM users WHERE username = ?;", (loginUsername,))
	data = cDB.fetchall()
	if data[0][0] == loginUsername and data[0][1] == loginPassword:
		print("Welcome, "+loginUsername+". You have successfully logged in!!")

	elif data[0][0] == loginUsername and data[0][1] != loginPassword:
		print("Wrong password, please try again")

	else:
		print("That user does not exist, sorry!")

def main():
	exitLoop = "y"
	while exitLoop == "y" or exitLoop == "Y" or exitLoop == "Yes":
		option = input("Please pick an option\n1 : Create an account\n2 : Login\nE : Exit\n")
		if option == "1":
			newUser()
		elif option == "2":
			loginUser()
		elif option == "E" or option == "e":
			exitLoop = "n"
		else:
			print("Please try again")

		if exitLoop == "y":
			exitLoop = input("Do you want to continue? [Y/N] ")

conDB = sqlite3.connect("/root/Desktop/python/random_scripts/login/user.db")
cDB = conDB.cursor()
cDB.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, password text)''')

main()
cDB.close() 
conDB.commit()